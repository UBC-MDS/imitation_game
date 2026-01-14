"""Tests for decrypt_symmetric function."""
import pytest
from imitation_game.decrypt_symmetric import decrypt_symmetric
from imitation_game.generate_symmetric_key import generate_symmetric_key

# Tests included:
# - test_decrypt_symmetric_basic_decryption: Basic decryption functionality with pre-defined keys
# - test_decrypt_symmetric_basic_decryption_generated_key: Basic decryption functionality with generated keys
# - test_decrypt_symmetric_empty_message: Decryption of empty message
# - test_decrypt_symmetric_long_message: Decryption fails for long message
# - test_decrypt_symmetric_invalid_key: Decryption with invalid key
# - test_decrypt_symmetric_unicode_message: Decryption of unicode message

class TestEncryptSymmetric:
    
    def test_decrypt_symmetric_basic_decryption():
        """Test basic decryption functionality with pre-defined keys."""
        key = b'524\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        message = "Hello, World!"
        expected = b'\x1a\x1d8\xd1\x0b\xfc\xc2\x8fb\x99\xf4-\x90'
        decrypted = decrypt_symmetric(message, key)
        assert decrypted == expected
        assert isinstance(decrypted, str)
        assert len(decrypted) > 0
        assert decrypted != message 

    def test_decrypt_symmetric_basic_decryption_generated_key(self):
        """Test basic decryption functionality with generated keys."""
        key = generate_symmetric_key()
        message = "Hello, World!"
        
        decrypted = decrypt_symmetric(message, key)
        
        assert isinstance(decrypted, str)
        assert len(decrypted) > 0
        assert decrypted != message   
    
    def test_decrypt_symmetric_empty_message(self):
        """Test decryption of empty message."""
        key = generate_symmetric_key()
        message = ""
        
        decrypted = decrypt_symmetric(message, key)
        
        assert isinstance(decrypted, str)
        assert len(decrypted) > 0
    
    def test_decrypt_symmetric_long_message(self):
        """Test decryption fails for message too long for AES."""
        key = generate_symmetric_key()
        message = "A" * 300
        
        with pytest.raises(ValueError, match="decryption failed"):
            decrypt_symmetric(message, key)
    
    def test_decrypt_symmetric_invalid_key(self):
        """Test decryption with invalid key."""
        message = "Hello, World!"
        invalid_key = "invalid_key"
        
        with pytest.raises(ValueError, match="decryption failed"):
            decrypt_symmetric(message, invalid_key)
    
    def test_decrypt_symmetric_unicode_message(self):
        """Test decryption of unicode message."""
        key = generate_symmetric_key()
        message = "Hello 🌍"
        
        decrypted = decrypt_symmetric(message, key)
        
        assert isinstance(decrypted, str)
        assert len(decrypted) > 0
        assert decrypted != message