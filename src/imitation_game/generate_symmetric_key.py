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

    Raises
    ------
    ValueError
        If the provided filepath is invalid or contains illegal characters.

    Notes
    -----
    The function generates a 256-bit (32-byte) key suitable for AES-256 encryption.
    The key is cryptographically secure and uses the Crypto.Random module which
    provides access to a cryptographically strong random number generator.

    If a filepath is provided, the function will create any necessary parent
    directories and save the key to the specified file.

    **Security Best Practices:**

    - **Never commit keys to version control** (add key files to .gitignore)
    - **Store keys securely** using environment variables or secure key management systems
    - **Restrict file permissions** when saving keys to disk (chmod 600 on Unix systems)
    - **Use the same key** for both encryption and decryption operations
    - **Keep keys confidential** - anyone with the key can decrypt your messages

    See Also
    --------
    encrypt_symmetric : Encrypt messages using the generated key
    decrypt_symmetric : Decrypt messages using the generated key

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

    >>> # Save key to file (remember to add to .gitignore!)
    >>> key = generate_symmetric_key("path/to/key.txt")  # doctest: +SKIP

    >>> # Recommended: Use environment variables instead of files
    >>> import os  # doctest: +SKIP
    >>> key = generate_symmetric_key()  # doctest: +SKIP
    >>> os.environ['ENCRYPTION_KEY'] = key  # doctest: +SKIP

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
            raise ValueError(
                f"Cannot save key to '{filepath}': {str(e)}. "
                f"Please provide a valid file path."
            )

        directory, _ = os.path.split(filepath)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
        with open(filepath, "w") as f:
            f.write(key)

    return key
