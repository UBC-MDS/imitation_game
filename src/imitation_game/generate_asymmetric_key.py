import os
from typing import Optional,Hashable
from Crypto.PublicKey import RSA
from random import randbytes, seed

def generate_asymmetric_key(public_filepath: Optional[str] = None, 
                            private_filepath: Optional[str] = None,
                            passphrase: Optional[Hashable] = None) -> tuple[bytes,bytes]:
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
    passphrase: Hashable, optional (default = None)
        Hashable argument to generate a consistent RSA key if required. If specified, `random.randbytes` will be used to
        generate the RSA key, otherwise `Crypto.Random.get_random_bytes` will be used.
        
    Returns
    -------
    public_key : bytes
        The key used for encryption outputted as a binary string; can be shared openly.
    private_key : bytes
        The key used for decryption outputted as a binary string; must be kept secret.
    """
    # Typechecks first
    if type(public_filepath) != str and public_filepath != None:
        raise TypeError(f"public_filepath must be of type str, received {type(public_filepath)}")
    if type(private_filepath) != str and private_filepath != None:
        raise TypeError(f"private_filepath must be of type str, received {type(private_filepath)}")
    if passphrase != None:
        try:
            hash(passphrase)
        except:
            raise TypeError(f"passphrase must be a hashable object, recived object of type {type(passphrase)}")
    
        
    # Obtain public and private keys
    key = None
    if passphrase != None: # use hash method
        seed(hash(passphrase))
        key = RSA.generate(2048,randfunc = randbytes)
    else: # use Crypto.Random.get_random_bytes
        key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()

    # Print out keys
    print("PUBLIC KEY:\n")
    print(public_key)
    print("PRIVATE KEY:\n")
    print(private_key)
    
    # Write keys to files if applicable
    if public_filepath != None:
        directory,filename = os.path.split(public_filepath)
        print(directory)
        if not os.path.exists(directory):
            os.makedirs(directory)
        with open(public_filepath, "wb") as f:
            f.write(public_key)
            
    if private_filepath != None:
        directory,filename = os.path.split(private_filepath)
        print(directory)
        if not os.path.exists(directory):
            os.makedirs(directory)
        with open(private_filepath, "wb") as f:
            f.write(private_key)
            
    return public_key,private_key

