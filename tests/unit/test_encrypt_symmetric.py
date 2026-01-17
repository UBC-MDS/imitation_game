"""Tests for encrypt_symmetric function."""
import pytest
from imitation_game.encrypt_symmetric import encrypt_symmetric
from imitation_game.generate_symmetric_key import generate_symmetric_key

# Tests included:
# - test_encrypt_symmetric_basic_encryption_generated_key: Basic encryption functionality with generated keys
# - test_encrypt_symmetric_empty_message: Encryption of empty message
# - test_encrypt_symmetric_long_message: Encryption fails for long message
# - test_encrypt_symmetric_invalid_key: Encryption with invalid key
# - test_encrypt_symmetric_unicode_message: Encryption of unicode message
# - test_encrypt_symmetric_key_from_file: Encryption using a key stored in a file

class TestEncryptSymmetric:

    def test_encrypt_symmetric_basic_encryption_generated_key(self):
        """Test basic encryption functionality with generated keys."""
        key = generate_symmetric_key()
        message = "Hello, World!"
        
        encrypted = encrypt_symmetric(message, key)
        
        assert isinstance(encrypted, str)
        assert len(encrypted) > 0
        assert encrypted != message
    
    def test_encrypt_symmetric_empty_message(self):
        """Test encryption of empty message."""
        key = generate_symmetric_key()
        message = ""
        
        encrypted = encrypt_symmetric(message, key)
        
        assert isinstance(encrypted, str)
        assert len(encrypted) > 0
    
    def test_encrypt_symmetric_long_message(self):
        """Test encryption fails for message too long for AES."""
        key = generate_symmetric_key()
        message = "A" * 300
        
        with pytest.raises(ValueError, match="Encryption failed"):
            encrypt_symmetric(message, key)
    
    def test_encrypt_symmetric_invalid_key(self):
        """Test encryption with invalid key."""
        message = "Hello, World!"
        invalid_key = "invalid_key"
        
        with pytest.raises(ValueError, match="Encryption failed"):
            encrypt_symmetric(message, invalid_key)
    
    def test_encrypt_symmetric_unicode_message(self):
        """Test encryption of unicode message."""
        key = generate_symmetric_key()
        message = "Hello 🌍"
        
        encrypted = encrypt_symmetric(message, key)
        
        assert isinstance(encrypted, str)
        assert len(encrypted) > 0
        assert encrypted != message

    def test_encrypt_symmetric_key_from_file(self, tmp_path):
        """Test encryption using a key stored in a file."""
        # Create a key file
        key_file = tmp_path / "secret.key"
        
        # Generate and save the key to the file
        original_key = generate_symmetric_key(str(key_file))
        
        message = "Secret message via file"
        encrypted = encrypt_symmetric(message, str(key_file))
        
        assert isinstance(encrypted, str)
        assert len(encrypted) > 0
        
        encrypted_alt = encrypt_symmetric(message, original_key)
        assert isinstance(encrypted_alt, str)