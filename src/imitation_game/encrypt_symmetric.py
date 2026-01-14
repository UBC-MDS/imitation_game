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
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext = cipher.encrypt(message)
    return ciphertext