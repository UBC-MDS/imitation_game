import base64
import os
from Crypto.Cipher import AES


def encrypt_symmetric(message, key):
    """
    Encrypts a plaintext message using AES in Counter (CTR) mode.

    Parameters
    ----------
    message : str
        The human-readable string to be encrypted.
        Must be 256 characters or fewer.
    key : str
        The shared secret key. If a string is provided,
        it must be Base64 encoded.
        OR a path to a file containing the key.

    Returns
    -------
    str
        A Base64-encoded string containing the 8-byte nonce followed by
        the ciphertext.

    Raises
    ------
    ValueError
        If the key is not properly Base64 encoded, the message exceeds 256
        characters, or the key length is invalid for AES.

    See Also
    --------
    generate_symmetric_key : Function used to create a valid key.

    Notes
    -----
    This function uses AES-CTR mode. CTR mode turns a block cipher into
    a stream cipher. It generates a unique nonce for every encryption
    call, meaning the same plaintext will produce different ciphertext
    every time it is encrypted with the same key.

    Examples
    --------
    >>> # Basic encryption with key
    >>> from imitation_game.generate_symmetric_key \
    ... import generate_symmetric_key
    >>> from imitation_game.encrypt_symmetric import encrypt_symmetric
    >>> key = generate_symmetric_key()
    >>> msg = "Top Secret"
    >>> encrypted = encrypt_symmetric(msg, key)
    >>> encrypted
    'X0QsE3P0MVblGhPOWKdrgbaD'

    >>> # CTR mode produces different results for the same input
    >>> key = generate_symmetric_key()
    >>> enc1 = encrypt_symmetric("Top Secret", key)
    >>> enc2 = encrypt_symmetric("Top Secret", key)
    >>> enc1 == enc2
    False

    >>> # Encryption using a key file
    >>> key_path = "secret.key"
    >>> generate_symmetric_key(key_path)
    >>> msg = "Top Secret"
    >>> encrypted = encrypt_symmetric(msg, key_path)
    >>> isinstance(encrypted, str)
    True

    >>> # Encryption using an existing key file
    >>> with open("secret.key", "w") as f:
    ...     f.write("aNa/PmjyUk2hrFFm+lqOTFE/nPhi+elUFg3SGt6EETg=")
    >>> encrypted = encrypt_symmetric("Top Secret", "secret.key")
    >>> encrypted
    '0rH1lkuVpskHbqMkgAOx0+pd'
    """
    if isinstance(key, str) and os.path.isfile(key):
        with open(key, 'r') as f:
            key = f.read().strip()

    if isinstance(key, str):
        try:
            key = base64.b64decode(key)
        except Exception:
            raise ValueError("Encryption failed: Invalid key encoding")

    if len(message) > 256:
        raise ValueError("Encryption failed: Message too long")

    cipher = AES.new(key, AES.MODE_CTR)
    ciphertext = cipher.encrypt(message.encode())
    return base64.b64encode(cipher.nonce + ciphertext).decode('utf-8')
