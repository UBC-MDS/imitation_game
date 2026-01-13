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
    # Typecheck first

    # Actual key generation here

    return "",""

if __name__ == "__main__":
    # example testing from https://www.pycryptodome.org/src/examples
    # debug code to remove before making PR
    generate_asymmetric_key(0,8,[8,7,6]) # typechecking will be needed
    seed(448)
    key = RSA.generate(2048,randfunc = randbytes)
    private_key = key.export_key()
    with open("private.pem", "wb") as f:
        f.write(private_key)
    
    public_key = key.publickey().export_key()
    with open("receiver.pem", "wb") as f:
        f.write(public_key)
    print(public_key)
    print()
    print(private_key)

    print(type(public_key))

    with open("private.pem", "rb") as f:
        x = f.read()
    print(x)
    assert x == private_key