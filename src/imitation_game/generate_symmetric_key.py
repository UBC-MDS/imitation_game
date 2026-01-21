from Crypto.Random import get_random_bytes
import base64
import os
from typing import Optional
from pathvalidate import validate_filepath, ValidationError


def generate_symmetric_key(filepath: Optional[str] = None) -> str:
    """
    Generate a cryptographically secure random key for symmetric encryption.
    
    This function creates a URL-safe base64-encoded key that can be used 
    with symmetric encryption algorithms. The key is generated using secure 
    random number generation to ensure cryptographic strength.
    
    Parameters
    ----------
    filepath : str, optional (default = None)
        Filepath to save the generated key. If no filepath is specified, 
        the key will not be saved to a file.

    Returns
    -------
    str
        A base64-encoded string representing the encryption key. This key 
        should be kept secret and used for both encryption and decryption.
    
    Notes
    -----
    The function generates a 256-bit (32-byte) key suitable for AES-256 encryption.
    The key is cryptographically secure and uses the Crypto.Random module which
    provides access to a cryptographically strong random number generator.
    
    If a filepath is provided, the function will create any necessary parent 
    directories and save the key to the specified file.

    Examples
    --------
    >>> key = generate_symmetric_key()
    >>> isinstance(key, str)
    True
    >>> len(key) > 0
    True
    
    >>> # Generate multiple keys - each should be unique
    >>> key1 = generate_symmetric_key()
    >>> key2 = generate_symmetric_key()
    >>> key1 != key2
    True
    
    >>> # Practical usage: Generate and store a key
    >>> encryption_key = generate_symmetric_key()
    >>> # Store this key securely - it will be needed for both encryption and decryption
    >>> print(f"Generated key: {encryption_key[:10]}...")  # doctest: +SKIP
    Generated key: aB3dEf7gH9...
    
    >>> # Save key to file
    >>> key = generate_symmetric_key("path/to/key.txt")  # doctest: +SKIP

    """
    # Generate 32 bytes (256 bits) of random data for AES-256 encryption
    random_bytes = get_random_bytes(32)
    
    # Encode to base64 for easy storage and transmission
    key = base64.b64encode(random_bytes).decode('utf-8')
    
    # Write key to file if filepath is provided
    if filepath is not None:
        # Validate the filepath to catch issues early
        try:
            validate_filepath(filepath, platform="auto")
        except ValidationError as e:
            raise ValueError(f"Invalid filepath: {e}")
        
        directory, _ = os.path.split(filepath)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
        with open(filepath, "w") as f:
            f.write(key)
    
    return key



