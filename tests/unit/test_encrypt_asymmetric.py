import pytest
import tempfile
import os
from imitation_game.encrypt_asymmetric import encrypt_asymmetric
from imitation_game.generate_asymmetric_key import generate_asymmetric_key

# NOTE: All tests in this file were suggested by Amazon Q Developer
# Tests included:
# - test_encrypt_asymmetric_basic: Basic encryption functionality with sender/receiver keys
# - test_encrypt_asymmetric_empty_message: Encryption of empty message
# - test_encrypt_asymmetric_long_message: Encryption fails for message too
#   long for RSA 2048 can encrypt max ~245 bytes, create longer message
# - test_encrypt_asymmetric_invalid_receiver_key: Encryption with invalid receiver public key
# - test_encrypt_asymmetric_invalid_sender_key: Encryption with invalid sender private key
# - test_encrypt_asymmetric_unicode_message: Encryption of unicode message


class TestEncryptAsymmetric:

    def test_encrypt_asymmetric_basic(self):
        """Test basic encryption functionality with sender/receiver keys."""
        sender_private, sender_public = generate_asymmetric_key()
        receiver_private, receiver_public = generate_asymmetric_key()
        message = "Hello, World!"

        encrypted = encrypt_asymmetric(message, receiver_public, sender_private)

        assert isinstance(encrypted, str)
        assert len(encrypted) > 0
        assert encrypted != message

    def test_encrypt_asymmetric_empty_message(self):
        """Test encryption of empty message."""
        sender_private, sender_public = generate_asymmetric_key()
        receiver_private, receiver_public = generate_asymmetric_key()
        message = ""

        encrypted = encrypt_asymmetric(message, receiver_public, sender_private)

        assert isinstance(encrypted, str)
        assert len(encrypted) > 0

    def test_encrypt_asymmetric_long_message(self):
        """Test encryption fails for message too long for RSA."""
        sender_private, sender_public = generate_asymmetric_key()
        receiver_private, receiver_public = generate_asymmetric_key()
        message = "A" * 300

        with pytest.raises(ValueError, match="Encryption failed"):
            encrypt_asymmetric(message, receiver_public, sender_private)

    def test_encrypt_asymmetric_invalid_receiver_key(self):
        """Test encryption with invalid receiver public key."""
        sender_private, sender_public = generate_asymmetric_key()
        message = "Hello, World!"
        invalid_key = "invalid_key"

        with pytest.raises(ValueError, match="Encryption failed"):
            encrypt_asymmetric(message, invalid_key, sender_private)

    def test_encrypt_asymmetric_invalid_sender_key(self):
        """Test encryption with invalid sender private key."""
        receiver_private, receiver_public = generate_asymmetric_key()
        message = "Hello, World!"
        invalid_key = "invalid_key"

        with pytest.raises(ValueError, match="Encryption failed"):
            encrypt_asymmetric(message, receiver_public, invalid_key)

    def test_encrypt_asymmetric_unicode_message(self):
        """Test encryption of unicode message."""
        sender_private, sender_public = generate_asymmetric_key()
        receiver_private, receiver_public = generate_asymmetric_key()
        message = "Hello 🌍"

        encrypted = encrypt_asymmetric(message, receiver_public, sender_private)

        assert isinstance(encrypted, str)
        assert len(encrypted) > 0
        assert encrypted != message

    def test_encrypt_asymmetric_with_file_paths(self):
        """Test encryption using file paths for keys."""
        sender_private, sender_public = generate_asymmetric_key()
        receiver_private, receiver_public = generate_asymmetric_key()
        message = "Hello, World!"

        with tempfile.TemporaryDirectory() as tmpdir:
            receiver_pub_path = os.path.join(tmpdir, "receiver_public.pem")
            sender_priv_path = os.path.join(tmpdir, "sender_private.pem")

            with open(receiver_pub_path, 'wb') as f:
                f.write(receiver_public)
            with open(sender_priv_path, 'wb') as f:
                f.write(sender_private)

            encrypted = encrypt_asymmetric(message, receiver_pub_path, sender_priv_path)

            assert isinstance(encrypted, str)
            assert len(encrypted) > 0
            assert encrypted != message
