import base64
from Crypto.Cipher import AES

def encrypt_symmetric(message, key, file_path=None):
    """
    Encrypts a plaintext message using a symmetric key.

    Parameters
    ----------
    message : str
        The human-readable string to be encrypted.
    key : str
        The shared secret key used for encryption.

    Returns
    -------
    str
        The encrypted ciphertext.
    """
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