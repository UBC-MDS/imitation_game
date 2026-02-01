from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import base64
import json
import os
from typing import Union


def decrypt_asymmetric(
    encrypted_data: str,
    receiver_private_key: Union[bytes, str],
    sender_public_key: Union[bytes, str],
) -> str:
    """
    Decrypts a message using the receiver's private key and verifies the
    signature using the sender's public key. This ensures both confidentiality
    (only receiver can decrypt) and authenticity (verifies sender identity).

    Parameters
    ----------
    encrypted_data : str
        Base64-encoded JSON containing encrypted message and signature.
    receiver_private_key : bytes or str
        The receiver's RSA private key in PEM format (bytes) or path to key file
        (str).
    sender_public_key : bytes or str
        The sender's RSA public key in PEM format (bytes) or path to key file
        (str) for signature verification.

    Returns
    -------
    str
        The decrypted and verified plaintext message.

    Raises
    ------
    ValueError
        If decryption fails, signature verification fails, or keys are invalid.

    Examples
    --------
    >>> from imitation_game.generate_asymmetric_key import generate_asymmetric_key
    >>> from imitation_game.encrypt_asymmetric import encrypt_asymmetric
    >>> from imitation_game.decrypt_asymmetric import decrypt_asymmetric
    >>> receiver_public, receiver_private = generate_asymmetric_key()
    >>> sender_public, sender_private = generate_asymmetric_key()
    >>> encrypted = encrypt_asymmetric(
    ...     "Hello, world!",
    ...     receiver_public,
    ...     sender_private,
    ... )
    >>> decrypt_asymmetric(encrypted, receiver_private, sender_public)
    'Hello, world!'
    """
    # Load receiver private key
    try:
        if isinstance(receiver_private_key, str) and os.path.isfile(
            receiver_private_key
        ):
            with open(receiver_private_key, 'rb') as f:
                receiver_key = RSA.import_key(f.read())
        else:
            receiver_key = RSA.import_key(receiver_private_key)
    except (ValueError, IndexError, TypeError) as e:
        raise ValueError(f"Invalid receiver private key: {str(e)}")

    # Load sender public key
    try:
        if isinstance(sender_public_key, str) and os.path.isfile(sender_public_key):
            with open(sender_public_key, 'rb') as f:
                sender_key = RSA.import_key(f.read())
        else:
            sender_key = RSA.import_key(sender_public_key)
    except (ValueError, IndexError, TypeError) as e:
        raise ValueError(f"Invalid sender public key: {str(e)}")

    try:
        # Decode the encrypted data
        try:
            decoded_payload = base64.b64decode(encrypted_data.encode('utf-8'))
            data = json.loads(decoded_payload.decode('utf-8'))
            encrypted_message = base64.b64decode(
                data['encrypted_message'].encode('utf-8')
            )
            signature = base64.b64decode(data['signature'].encode('utf-8'))
        except (json.JSONDecodeError, KeyError, IndexError,  Exception):
            raise ValueError("Invalid encrypted data format")

        # Decrypt with receiver's private key
        try:
            cipher = PKCS1_OAEP.new(receiver_key)
            decrypted_bytes = cipher.decrypt(encrypted_message)
            message = decrypted_bytes.decode('utf-8')
        except ValueError as e:
            raise ValueError(f"Decryption failed (incorrect key?): {str(e)}")

        # Verify signature with sender's public key
        message_hash = SHA256.new(message.encode('utf-8'))
        try:
            pkcs1_15.new(sender_key).verify(message_hash, signature)
        except (ValueError, TypeError):
            raise ValueError(
                "Signature verification failed - message may be tampered with "
                "or from wrong sender"
            )

        return message
    except ValueError:
        raise
    except Exception as e:
        raise ValueError(f"Unexpected decryption error: {str(e)}")
