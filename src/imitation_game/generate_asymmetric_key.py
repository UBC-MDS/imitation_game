import os
from typing import Optional, Hashable
from Crypto.PublicKey import RSA
from random import randbytes, seed
from pathvalidate import ValidationError, validate_filepath


def generate_asymmetric_key(private_filepath: Optional[str] = None,
                            public_filepath: Optional[str] = None,
                            passphrase: Optional[Hashable] = None) -> tuple[bytes, bytes]:
    r"""
    Generates a pair of RSA keys for asymmetric encryption.

    The public and private key will be printed out for the user to copy.
    If output filepath parameters are passed then the public and private
    keys will be saved to their respective filepaths.

    Parameters
    ----------
    private_filepath : str, optional (default = None)
        Filepath to save the private key in. If no filepath is specified
        the private key will not be saved in a file.
    public_filepath : str, optional (default = None)
        Filepath to save the public key in. If no filepath is specified
        the public key will not be saved in a file.
    passphrase: Hashable, optional (default = None)
        Hashable argument to generate a consistent RSA key if required.
        If specified, `random.randbytes` will be used to generate the
        RSA key, otherwise `Crypto.Random.get_random_bytes` will be used.

    Returns
    -------
    private_key : bytes
        The key used for decryption outputted as a binary string; must be
        kept secret.
    public_key : bytes
        The key used for encryption outputted as a binary string; can be
        shared openly.

    Examples
    --------
    >>> from imitation_game.generate_asymmetric_key import generate_asymmetric_key
    >>> private_key,public_key = generate_asymmetric_key()
    PRIVATE KEY:
    <BLANKLINE>
    b'-----BEGIN RSA PRIVATE KEY-----\nMIIEpAIBAA...La1DC1VOvQ==\n-----END RSA PRIVATE KEY-----'
    PUBLIC KEY:
    <BLANKLINE>
    b'-----BEGIN PUBLIC KEY-----\nMIIBIjANBg...f\n9wIDAQAB\n-----END PUBLIC KEY-----'
    >>> private_key
    b'-----BEGIN RSA PRIVATE KEY-----\nMIIEpAIBAA...La1DC1VOvQ==\n-----END RSA PRIVATE KEY-----'
    >>> public_key
    b'-----BEGIN PUBLIC KEY-----\nMIIBIjANBg...f\n9wIDAQAB\n-----END PUBLIC KEY-----'
    """

    """
    Google AI was used to initially research methods for determining if a
    specific function for checking if a file path is valid without creating it
    through the interaction link https://share.google/aimode/z9UkOkSuMRvZHfhEr,

    This resulted in finding the python package pathvalidate
    (https://pypi.org/project/pathvalidate/) which is utilized
    for this testcase and the specific path validation check.
    """
    # Typechecks and path validation where applicable
    if private_filepath is not None:
        if isinstance(private_filepath, str):
            errormsg = f"private_filepath must be of type str, received {type(private_filepath)}"
            raise TypeError(errormsg)
        try:
            validate_filepath(private_filepath)
        except ValidationError as ve:
            raise ve
    if public_filepath is not None:
        if isinstance(public_filepath, str):
            errormsg = f"public_filepath must be of type str, received {type(public_filepath)}"
            raise TypeError(errormsg)
        try:
            validate_filepath(public_filepath)
        except ValidationError as ve:
            raise ve
    if passphrase is not None:
        try:
            hash(passphrase)
        except TypeError:
            errormsg = f"passphrase must be hashable, received type {type(passphrase)}"
            raise TypeError(errormsg)

    # Obtain public and private keys
    key = None
    if passphrase is not None:  # use hash method
        seed(hash(passphrase))
        key = RSA.generate(2048, randfunc=randbytes)
    else:  # use Crypto.Random.get_random_bytes
        key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()

    # Print out keys
    print("PRIVATE KEY:\n")
    print(private_key)
    print("PUBLIC KEY:\n")
    print(public_key)

    # Write keys to files if applicable
    if private_filepath is not None:
        directory, _ = os.path.split(private_filepath)
        print(directory)
        if not os.path.exists(directory):
            os.makedirs(directory)
        with open(private_filepath, "wb") as f:
            f.write(private_key)
    if public_filepath is not None:
        directory, _ = os.path.split(public_filepath)
        print(directory)
        if not os.path.exists(directory):
            os.makedirs(directory)
        with open(public_filepath, "wb") as f:
            f.write(public_key)

    return private_key, public_key
