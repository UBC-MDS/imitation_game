from typing import Optional

def generate_asymmetric_key(public_filepath: Optional[str] = None, private_filepath: Optional[str] = None) -> tuple[str,str]:
    """
    Generates a pair of RSA keys for asymmetric encryption.

    The public and private key will be printed out for the user to copy.
    If output filepath parameters are passed then the public and private
    keys will be saved to their respective filepaths.
    
    Parameters
    ----------
    public_filepath : str, optional (default = None)
        Filepath to save the public key in. If no filepath is specified the public key will not be saved in a file.
    private_filepath : str, optional (default = None)
        Filepath to save the private key in. If no filepath is specified the private key will not be saved in a file.
    
    Returns
    -------
    public_key : str
        The key used for encryption; can be shared openly.
    private_key : str
        The key used for decryption; must be kept secret.
    """
    return "",""

