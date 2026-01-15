"""Integration tests for asymmetric encryption and decryption."""
import pytest
import os

from imitation_game.generate_asymmetric_key import generate_asymmetric_key
from imitation_game.encrypt_asymmetric import encrypt_asymmetric
from imitation_game.decrypt_asymmetric import decrypt_asymmetric


# NOTE: All tests in this file were suggested by LLM
# Tests included:
# - test_encrypt_decrypt_roundtrip: Complete encrypt-decrypt roundtrip with sender/receiver key pairs
# - test_encrypt_decrypt_roundtrip_with_file_paths: test_encrypt_decrypt_roundtrip utilizing file paths
# - test_technically_asymmetric: Run through full encryption-decryption setup where sender/receiver key pairs are identical

test_directory = "tests/asymmetric_integration"
class TestAsymmetricIntegration:
    def test_encrypt_decrypt_roundtrip(self):
        """Test complete encrypt-decrypt roundtrip with sender/receiver key pairs."""
        sender_private, sender_public = generate_asymmetric_key()
        receiver_private, receiver_public = generate_asymmetric_key()
        message = "Hello, World!"
        
        encrypted = encrypt_asymmetric(message, receiver_public, sender_private)
        decrypted = decrypt_asymmetric(encrypted, receiver_private, sender_public)
        
        assert decrypted == message

    def test_encrypt_decrypt_roundtrip_with_file_paths(self):
        """Test encryption using file paths for keys."""

        # create paths
        sender_private_path = os.path.join(test_directory,"sender_private.pem")
        sender_public_path = os.path.join(test_directory,"sender_public.pem")
        receiver_private_path = os.path.join(test_directory,"sender_private.pem")
        receiver_public_path = os.path.join(test_directory,"sender_public.pem")
        
        # generate keys to paths
        generate_asymmetric_key(sender_private_path,sender_public_path)
        generate_asymmetric_key(receiver_private_path,receiver_public_path)
        message = "Hello again! This is another test"
        
        # encrypt/decrypt from files
        encrypted = encrypt_asymmetric(message, receiver_public_path, sender_private_path)
        decrypted = decrypt_asymmetric(encrypted, receiver_private_path, sender_public_path)
        
        assert decrypted == message
        
