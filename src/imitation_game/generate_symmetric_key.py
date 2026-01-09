def generate_symmetric_key():
    """
    Generate a cryptographically secure random key for symmetric encryption.
    
    This function creates a URL-safe base64-encoded key that can be used 
    with symmetric encryption algorithms. The key is generated using secure 
    random number generation to ensure cryptographic strength.

    Returns
    -------
    str
        A base64-encoded string representing the encryption key. This key 
        should be kept secret and used for both encryption and decryption.

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

    """
    pass
