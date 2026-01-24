from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import base64
import json
import os
from typing import Union

def encrypt_asymmetric(message: str, receiver_public_key: Union[bytes, str], sender_private_key: Union[bytes, str]) -> str:
    """
    Encrypts a message using the receiver's public key and signs it with the sender's private key.
    This ensures both confidentiality (only receiver can decrypt) and authenticity (receiver can verify sender).
    
    Parameters
    ----------
    message : str
        The plaintext message to encrypt.
    receiver_public_key : bytes or str
        The receiver's RSA public key in PEM format (bytes) or path to key file (str).
    sender_private_key : bytes or str
        The sender's RSA private key in PEM format (bytes) or path to key file (str) for signing.
        
    Returns
    -------
    str
        Base64-encoded JSON containing encrypted message and signature.
        
    Raises
    ------
    ValueError
        If the message is too long for RSA encryption or keys are invalid.

    Examples
    --------
    >>> from imitation_game.generate_asymmetric_key import generate_asymmetric_key
    >>> from imitation_game.encrypt_asymmetric import encrypt_asymmetric
    >>> receiver_public, _ = generate_asymmetric_key()
    >>> _, sender_private = generate_asymmetric_key()
    >>> encrypted = encrypt_asymmetric("Hello, world!", receiver_public, sender_private)
    """
    try:
        # Load receiver public key
        if isinstance(receiver_public_key, str) and os.path.isfile(receiver_public_key):
            with open(receiver_public_key, 'rb') as f:
                receiver_key = RSA.import_key(f.read())
        else:
            receiver_key = RSA.import_key(receiver_public_key)
        
        # Load sender private key
        if isinstance(sender_private_key, str) and os.path.isfile(sender_private_key):
            with open(sender_private_key, 'rb') as f:
                sender_key = RSA.import_key(f.read())
        else:
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
