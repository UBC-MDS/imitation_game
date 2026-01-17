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
# - test_key_file_persistence_integration: Test the full lifecycle using a physical file

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

    def test_key_file_persistence_integration(self, tmp_path):
        """
        Test the full lifecycle using a physical file:
        1. Generate key to a file.
        2. Encrypt a message using the file path.
        3. Decrypt the message using the file path.
        """
        # Create a key file
        key_file = tmp_path / "secret.key"
        key_file_path = str(key_file)

        # 1. Generate and save
        original_key_string = generate_symmetric_key(key_file_path)
        
        # Verify the file actually exists and contains the key
        assert key_file.exists()
        assert key_file.read_text().strip() == original_key_string

        # 2. Encrypt using key file
        message = "Integration test for file-based keys."
        ciphertext = encrypt_symmetric(message, key_file_path)
        
        # 3. Decrypt using key file
        decrypted = decrypt_symmetric(ciphertext, key_file_path)

        assert decrypted == message
        assert decrypted != ciphertext