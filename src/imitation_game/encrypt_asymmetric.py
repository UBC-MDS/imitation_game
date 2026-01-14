from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import base64
import json

def encrypt_asymmetric(message: str, receiver_public_key: bytes, sender_private_key: bytes) -> str:
    """
    Encrypts a message using the receiver's public key and signs it with the sender's private key.
    This ensures both confidentiality (only receiver can decrypt) and authenticity (receiver can verify sender).
    
    Parameters
    ----------
    message : str
        The plaintext message to encrypt.
    receiver_public_key : bytes
        The receiver's RSA public key in PEM format.
    sender_private_key : bytes
        The sender's RSA private key in PEM format for signing.
        
    Returns
    -------
    str
        Base64-encoded JSON containing encrypted message and signature.
        
    Raises
    ------
    ValueError
        If the message is too long for RSA encryption or keys are invalid.
    """
    try:
        # Import keys
        receiver_key = RSA.import_key(receiver_public_key)
        sender_key = RSA.import_key(sender_private_key)
        
        # Encrypt with receiver's public key
        cipher = PKCS1_OAEP.new(receiver_key)
        encrypted_bytes = cipher.encrypt(message.encode('utf-8'))
        
        # Sign with sender's private key
        message_hash = SHA256.new(message.encode('utf-8'))
        signature = pkcs1_15.new(sender_key).sign(message_hash)
        
        # Combine encrypted message and signature
        result = {
            'encrypted_message': base64.b64encode(encrypted_bytes).decode('utf-8'),
            'signature': base64.b64encode(signature).decode('utf-8')
        }
        
        return base64.b64encode(json.dumps(result).encode('utf-8')).decode('utf-8')
    except Exception as e:
        raise ValueError(f"Encryption failed: {str(e)}")
