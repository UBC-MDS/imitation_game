"""Tests for decrypt_symmetric function."""
import pytest
from imitation_game.encrypt_symmetric import encrypt_symmetric
from imitation_game.decrypt_symmetric import decrypt_symmetric
from imitation_game.generate_symmetric_key import generate_symmetric_key

# Tests included:
# - test_decrypt_symmetric_basic: Test basic decryption functionality with key
# - test_decrypt_symmetric_empty_message: Test decryption of empty message
# - test_decrypt_symmetric_unicode_message: Test decryption of unicode message
# - test_decrypt_symmetric_wrong_key: Test decryption with wrong key
# - test_decrypt_symmetric_invalid_data: Test decryption with invalid encrypted data
# - test_decrypt_symmetric_invalid_key: Test decryption with invalid key
# - test_decrypt_symmetric_key_from_file: Test decryption using a key stored in a file

class TestDecryptSymmetric:
    
    def test_decrypt_symmetric_basic(self):
        """Test basic decryption functionality with key."""
        key = generate_symmetric_key()
        message = "Hello, World!"
        
        encrypted = encrypt_symmetric(message, key)
        decrypted = decrypt_symmetric(encrypted, key)
        
        assert decrypted == message
    
    def test_decrypt_symmetric_empty_message(self):
        """Test decryption of empty message."""
        key = generate_symmetric_key()
        message = ""
        
        encrypted = encrypt_symmetric(message, key)
        decrypted = decrypt_symmetric(encrypted, key)
        
        assert decrypted == message
    
    def test_decrypt_symmetric_unicode_message(self):
        """Test decryption of unicode message."""
        key = generate_symmetric_key()
        message = "Hello 🌍"
        
        encrypted = encrypt_symmetric(message, key)
        decrypted = decrypt_symmetric(encrypted, key)
        
        assert decrypted == message
    
    def test_decrypt_symmetric_wrong_key(self):
        """Test decryption with wrong key."""
        key1 = generate_symmetric_key()
        key2 = generate_symmetric_key()
        message = "Hello, World!"
        
        encrypted = encrypt_symmetric(message, key1)
        
        with pytest.raises(ValueError, match="Decryption failed"):
            decrypt_symmetric(encrypted, key2)
    
    def test_decrypt_symmetric_invalid_data(self):
        """Test decryption with invalid encrypted data."""
        key = generate_symmetric_key()
        invalid_encrypted = "invalid_encrypted_message"
        
        with pytest.raises(ValueError, match="Decryption failed"):
            decrypt_symmetric(invalid_encrypted, key)
    
    def test_decrypt_symmetric_invalid_key(self):
        """Test decryption with invalid key."""
        key = generate_symmetric_key()
        message = "Hello, World!"
        encrypted = encrypt_symmetric(message, key)
        invalid_key = "invalid_key"
        
        with pytest.raises(ValueError, match="Decryption failed"):
            decrypt_symmetric(encrypted, invalid_key)

    def test_decrypt_symmetric_key_from_file(self, tmp_path):
        """Test decryption using a key stored in a file."""
        # Create a key file
        key_file = tmp_path / "secret.key"
        key_file_path = str(key_file)
        
        generate_symmetric_key(key_file_path)
        message = "Testing the file-based round trip!"

        encrypted = encrypt_symmetric(message, key_file_path)
        decrypted = decrypt_symmetric(encrypted, key_file_path)
        
        assert decrypted == message
        assert isinstance(decrypted, str)