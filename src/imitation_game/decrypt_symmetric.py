import base64
from Crypto.Cipher import AES

def decrypt_symmetric(ciphertext, key):
    """
    Decrypts an AES-CTR encrypted message and restores it to plaintext.

    Parameters
    ----------
    ciphertext : str
        The Base64-encoded string to be decrypted. This must contain the 
        8-byte nonce followed by the actual encrypted data.
    key : str
        The shared secret key. If a string is provided, it must be Base64 
        encoded.

    Returns
    -------
    str
        The original plaintext message, UTF-8 decoded.

    Raises
    ------
    ValueError
        If the key or ciphertext is not valid Base64, if the key length is 
        incorrect, or if the data cannot be decoded as UTF-8 after decryption.

    See Also
    --------
    encrypt_symmetric : The counterpart function used to create the ciphertext.

    Notes
    -----
    The function extracts the first 8 bytes of the decoded ciphertext to use 
    as the nonce. This must match the nonce generated during encryption for 
    the process to succeed.

    Examples
    --------
    >>> from imitation_game.generate_symmetric_key import generate_symmetric_key
    >>> from imitation_game.encrypt_symmetric import encrypt_symmetric
    >>> from imitation_game.decrypt_symmetric import decrypt_symmetric
    >>> key = generate_symmetric_key()
    >>> ciphertext = encrypt_symmetric("Top Secret", key)
    >>> decrypt_symmetric(ciphertext, key)
    'Top Secret'
    """
    try:
        if isinstance(key, str):
            key = base64.b64decode(key)
        
        ciphertext_decoded = base64.b64decode(ciphertext)

        nonce = ciphertext_decoded[:8]
        ciphertext = ciphertext_decoded[8:]

        cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
        decrypted_bytes = cipher.decrypt(ciphertext)

        return decrypted_bytes.decode('utf-8')

    except Exception as e:
        raise ValueError(f"Decryption failed: {str(e)}")
