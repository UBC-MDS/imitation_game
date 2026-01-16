"""Integration tests for symmetric encryption and decryption."""
import base64
import pytest

from imitation_game.generate_symmetric_key import generate_symmetric_key
from imitation_game.encrypt_symmetric import encrypt_symmetric
from imitation_game.decrypt_symmetric import decrypt_symmetric

# NOTE: All tests in this file were suggested by LLM
# Tests included:
# - test_encrypt_decrypt_integration: Test a message can be encrypted and then decrypted back to original
# - test_invalid_decryption_attempts: Test encrypt a message and confirm the wrong key cannot decrypt it

class TestAsymmetricIntegration:
    def test_encrypt_decrypt_integration(self):
        """Test a message can be encrypted and then decrypted back to original."""
        key = generate_symmetric_key()
        message = "Hello, World!"
        
        ciphertext = encrypt_symmetric(message, key)
        assert isinstance(ciphertext, str)
        assert ciphertext != message
        
        decrypted = decrypt_symmetric(ciphertext, key)
        
        # Final Verification
        assert decrypted == message

    def test_invalid_decryption_attempts(self):
        """Test encrypt a message and confirm the wrong key cannot decrypt it"""
        key1 = generate_symmetric_key()
        key2 = generate_symmetric_key()

        message = "Hello, World!"
        encrypted = encrypt_symmetric(message, key1)

        # wrong keys
        with pytest.raises(ValueError, match="Decryption failed"):
            decrypt_symmetric(encrypted, key2)
        
        # wrong nouce
        decoded = list(base64.b64decode(encrypted))
        decoded[0] = (decoded[0] + 1) % 256  # Flip a byte in the nonce section (first 8 bytes)
        tampered_encrypted = base64.b64encode(bytes(decoded)).decode('utf-8')
        
        with pytest.raises(ValueError, match="Decryption failed"):
            decrypt_symmetric(tampered_encrypted, key1)
        
        # invalid key
        with pytest.raises(ValueError, match="Decryption failed"):
            decrypt_symmetric(encrypted, "Invalid key")