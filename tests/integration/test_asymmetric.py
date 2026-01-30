"""Integration tests for asymmetric encryption and decryption."""
import os
import pytest

from imitation_game.generate_asymmetric_key import generate_asymmetric_key
from imitation_game.encrypt_asymmetric import encrypt_asymmetric
from imitation_game.decrypt_asymmetric import decrypt_asymmetric


# NOTE: All tests in this file were suggested by LLM
# Tests included:
# - test_encrypt_decrypt_roundtrip
#   Complete encrypt-decrypt roundtrip with sender/receiver key pairs
# - test_encrypt_decrypt_roundtrip_with_file_paths
#   test_encrypt_decrypt_roundtrip utilizing file paths
# - test_invalid_decryption_attempts
#   Encrypy a message and confirm the wrong key pair cannot decrypt it.

test_directory = "tests/asymmetric_integration"


class TestAsymmetricIntegration:
    def test_encrypt_decrypt_roundtrip(self):
        """Test complete encrypt-decrypt roundtrip with sender/receiver key pairs."""
        sender_private, sender_public = generate_asymmetric_key(passphrase=448)
        receiver_private, receiver_public = generate_asymmetric_key(passphrase=844)
        message = "Hello, World!"

        encrypted = encrypt_asymmetric(message, receiver_public, sender_private)
        decrypted = decrypt_asymmetric(encrypted, receiver_private, sender_public)

        assert decrypted == message

    def test_encrypt_decrypt_roundtrip_with_file_paths(self):
        """Test encryption using file paths for keys."""

        # create paths
        sender_private_path = os.path.join(test_directory, "sender_private.pem")
        sender_public_path = os.path.join(test_directory, "sender_public.pem")
        receiver_private_path = os.path.join(test_directory, "sender_private.pem")
        receiver_public_path = os.path.join(test_directory, "sender_public.pem")

        # generate keys to paths
        generate_asymmetric_key(sender_private_path, sender_public_path)
        generate_asymmetric_key(receiver_private_path, receiver_public_path)
        message = "Hello again! This is another test"

        # encrypt/decrypt from files
        encrypted = encrypt_asymmetric(message, receiver_public_path, sender_private_path)
        decrypted = decrypt_asymmetric(encrypted, receiver_private_path, sender_public_path)

        assert decrypted == message

    def test_invalid_decryption_attempts(self):
        """Test various key pairs that should all be unable to decrypt the message"""
        sender_private, sender_public = generate_asymmetric_key()
        receiver_private, receiver_public = generate_asymmetric_key()
        wrong_private, wrong_public = generate_asymmetric_key()

        message = "123456789"
        encrypted = encrypt_asymmetric(message, receiver_public, sender_private)

        # wrong keys
        with pytest.raises(ValueError):
            decrypt_asymmetric(encrypted, wrong_private, sender_public)
        with pytest.raises(ValueError):
            decrypt_asymmetric(encrypted, receiver_private, wrong_public)

        # wrong order
        with pytest.raises(ValueError):
            decrypt_asymmetric(encrypted, sender_public, receiver_private)

        # not using keys
        with pytest.raises(ValueError):
            decrypt_asymmetric(encrypted, "is this a key?", sender_public)
        with pytest.raises(ValueError):
            decrypt_asymmetric(encrypted, receiver_private, "is this a key?")
