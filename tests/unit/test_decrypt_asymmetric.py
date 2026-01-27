import pytest
from imitation_game.encrypt_asymmetric import encrypt_asymmetric
from imitation_game.decrypt_asymmetric import decrypt_asymmetric
from imitation_game.generate_asymmetric_key import generate_asymmetric_key

# NOTE: All tests in this file were suggested by LLM
# Tests included:
# - test_decrypt_asymmetric_basic: Basic decryption functionality with sender/receiver keys
# - test_decrypt_asymmetric_empty_message: Decryption of empty message
# - test_decrypt_asymmetric_unicode_message: Decryption of unicode message
# - test_decrypt_asymmetric_wrong_receiver_key: Decryption with wrong receiver private key
# - test_decrypt_asymmetric_wrong_sender_key: Decryption with wrong sender
#   public key (signature verification fails)
# - test_decrypt_asymmetric_invalid_data: Decryption with invalid encrypted data
# - test_decrypt_asymmetric_invalid_receiver_key: Decryption with invalid receiver private key
# - test_decrypt_asymmetric_invalid_sender_key: Decryption with invalid sender public key
# - test_tampered_message_detection: Tampered messages are detected through
#   signature verification


class TestDecryptAsymmetric:

    def test_decrypt_asymmetric_basic(self):
        """Test basic decryption functionality with sender/receiver keys."""
        sender_private, sender_public = generate_asymmetric_key()
        receiver_private, receiver_public = generate_asymmetric_key()
        message = "Hello, World!"

        encrypted = encrypt_asymmetric(message, receiver_public, sender_private)
        decrypted = decrypt_asymmetric(encrypted, receiver_private, sender_public)

        assert decrypted == message

    def test_decrypt_asymmetric_empty_message(self):
        """Test decryption of empty message."""
        sender_private, sender_public = generate_asymmetric_key()
        receiver_private, receiver_public = generate_asymmetric_key()
        message = ""

        encrypted = encrypt_asymmetric(message, receiver_public, sender_private)
        decrypted = decrypt_asymmetric(encrypted, receiver_private, sender_public)

        assert decrypted == message

    def test_decrypt_asymmetric_unicode_message(self):
        """Test decryption of unicode message."""
        sender_private, sender_public = generate_asymmetric_key()
        receiver_private, receiver_public = generate_asymmetric_key()
        message = "Hello 🌍"

        encrypted = encrypt_asymmetric(message, receiver_public, sender_private)
        decrypted = decrypt_asymmetric(encrypted, receiver_private, sender_public)

        assert decrypted == message

    def test_decrypt_asymmetric_wrong_receiver_key(self):
        """Test decryption with wrong receiver private key."""
        sender_private, sender_public = generate_asymmetric_key()
        receiver1_private, receiver1_public = generate_asymmetric_key()
        receiver2_private, receiver2_public = generate_asymmetric_key()
        message = "Hello, World!"

        encrypted = encrypt_asymmetric(message, receiver1_public, sender_private)

        with pytest.raises(ValueError, match="Decryption failed"):
            decrypt_asymmetric(encrypted, receiver2_private, sender_public)

    def test_decrypt_asymmetric_wrong_sender_key(self):
        """Test decryption with wrong sender public key (signature verification fails)."""
        sender1_private, sender1_public = generate_asymmetric_key()
        sender2_private, sender2_public = generate_asymmetric_key()
        receiver_private, receiver_public = generate_asymmetric_key()
        message = "Hello, World!"

        encrypted = encrypt_asymmetric(message, receiver_public, sender1_private)

        with pytest.raises(ValueError, match="Signature verification failed"):
            decrypt_asymmetric(encrypted, receiver_private, sender2_public)

    def test_decrypt_asymmetric_invalid_data(self):
        """Test decryption with invalid encrypted data."""
        sender_private, sender_public = generate_asymmetric_key()
        receiver_private, receiver_public = generate_asymmetric_key()
        invalid_encrypted = "invalid_encrypted_message"

        with pytest.raises(ValueError, match="Decryption failed"):
            decrypt_asymmetric(invalid_encrypted, receiver_private, sender_public)

    def test_decrypt_asymmetric_invalid_receiver_key(self):
        """Test decryption with invalid receiver private key."""
        sender_private, sender_public = generate_asymmetric_key()
        receiver_private, receiver_public = generate_asymmetric_key()
        message = "Hello, World!"
        encrypted = encrypt_asymmetric(message, receiver_public, sender_private)
        invalid_key = "invalid_key"

        with pytest.raises(ValueError, match="Decryption failed"):
            decrypt_asymmetric(encrypted, invalid_key, sender_public)

    def test_decrypt_asymmetric_invalid_sender_key(self):
        """Test decryption with invalid sender public key."""
        sender_private, sender_public = generate_asymmetric_key()
        receiver_private, receiver_public = generate_asymmetric_key()
        message = "Hello, World!"
        encrypted = encrypt_asymmetric(message, receiver_public, sender_private)
        invalid_key = "invalid_key"

        with pytest.raises(ValueError, match="Decryption failed"):
            decrypt_asymmetric(encrypted, receiver_private, invalid_key)

    def test_tampered_message_detection(self):
        """Test that tampered messages are detected through signature verification."""
        sender_private, sender_public = generate_asymmetric_key()
        receiver_private, receiver_public = generate_asymmetric_key()
        message = "Original message"

        encrypted = encrypt_asymmetric(message, receiver_public, sender_private)

        # Tamper with the encrypted data by modifying a character
        tampered_encrypted = encrypted[:-1] + ('A' if encrypted[-1] != 'A' else 'B')

        with pytest.raises(ValueError):
            decrypt_asymmetric(tampered_encrypted, receiver_private, sender_public)
