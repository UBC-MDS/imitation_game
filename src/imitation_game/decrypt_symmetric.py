import base64
from Crypto.Cipher import AES

def decrypt_symmetric(ciphertext, key):
    """
    Restores an encrypted message back to plaintext using the same symmetric key.

    Parameters
    ----------
    ciphertext : str
        The encrypted data to be decrypted.
    key : str
        The shared secret key that was used to encrypt the data.

    Returns
    -------
    str
        The original plaintext message.
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