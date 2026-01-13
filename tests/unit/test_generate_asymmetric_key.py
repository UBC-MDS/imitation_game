"""Tests for generate_asymmetric_key function."""
from imitation_game.imitation_game import generate_asymmetric_key
import pytest
from random import randbytes, seed
from Crypto.PublicKey import RSA
import os

# Standard Use Cases

test_directory = "tests/asymmetric_key_tests"

# pre computed exact keys
seed(448)
key = RSA.generate(2048,randfunc = randbytes)
seed_448_privatekey = key.export_key()
seed_448_publickey = key.publickey().export_key()
    

def test_basic():
    """Test basic use case (no arguments) to ensure no syntax errors"""
    publickey,privatekey = generate_asymmetric_key(None, None, None)
    assert type(publickey) == bytes, "Public key returned is not a bytes type object"
    assert type(privatekey) == bytes, "Private key returned is not a bytes type object"

def test_write_to_file():
    """Test writing public and private key to files"""
    public_file = "public.pem"
    private_file = "private.pem"
    public_path = os.path.join(test_directory,public_file)
    private_path = os.path.join(test_directory,private_file)
    generate_asymmetric_key(public_path, private_path, None)
    assert os.path.isfile(public_path), "test_write_to_file does not generate the public key file"
    assert os.path.isfile(private_path), "test_write_to_file does not generate the private key file"

def test_write_only_public():
    """Test writing ONLY public key to file"""
    public_file = "public2.pem"
    private_file = "private2.pem"
    public_path = os.path.join(test_directory,public_file)
    private_path = os.path.join(test_directory,private_file)
    generate_asymmetric_key(public_path, None, None)
    assert os.path.isfile(public_path), "test_write_only_public does not generate the public key file"
    assert os.path.isfile(private_path) == False, "test_write_only_public generated the private key file (should not occur)"

def test_write_only_private():
    """Test writing ONLY private key to file"""
    public_file = "public3.pem"
    private_file = "private3.pem"
    public_path = os.path.join(test_directory,public_file)
    private_path = os.path.join(test_directory,private_file)
    generate_asymmetric_key(None, private_path, None)
    assert os.path.isfile(public_path), "test_write_only_private generated the public key file (should not occur)"
    assert os.path.isfile(private_path) == False, "test_write_only_private does not generate the private key file"


def test_passphrase():
    """Test that passphrase ALWAYS generates a consistent pair of keys"""
    publickey,privatekey = generate_asymmetric_key(None, None, 448)
    assert publickey == seed_448_publickey, "Public key generated from passphrase 448 does not match expected key."
    assert privatekey == seed_448_privatekey, "Private key generated from passphrase 448 does not match expected key."
    

def test_full():
    """Test with every possible optional argument"""
    public_file = "public_full.pem"
    private_file = "private_full.pem"
    public_path = os.path.join(test_directory,public_file)
    private_path = os.path.join(test_directory,private_file)
    generate_asymmetric_key(public_path, private_path, 448)
    assert os.path.isfile(public_path), "test_full does not generate the public key file"
    assert os.path.isfile(private_path), "test_full does not generate the private key file"

    # confirm files produce the RSA keys as expected
    public_read,private_read = None,None
    with open(public_path, "rb") as f:
        public_read = f.read()
    with open(private_path, "rb") as f:
        private_read = f.read()
    assert public_read == seed_448_publickey, "Public key read from file does not match pregenerated 448 public key."
    assert private_read == seed_448_privatekey, "Private key read from file does not match pregenerated 448 private key."
    

# Argument type errors

def test_wrong_type_public():
    """Test that function stops on wrong type in public_filepath"""
    with pytest.raises(TypeError):
        generate_asymmetric_key(False, None, None)

def test_wrong_type_private():
    """Test that function stops on wrong type in private_filepath"""
    with pytest.raises(TypeError):
        generate_asymmetric_key(None, 727, None)

def test_wrong_type_passphrase():
    """Test that function stops on wrong type in passphrase (List is NOT hashable)"""
    with pytest.raises(TypeError):
        generate_asymmetric_key(False, None, ["W","Y","S","I"])

