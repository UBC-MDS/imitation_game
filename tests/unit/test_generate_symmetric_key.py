"""Tests for generate_symmetric_key function."""
from imitation_game.generate_symmetric_key import generate_symmetric_key
import pytest
import base64

# Test Strategy:
# 1. Basic functionality tests - ensure function works without errors
# 2. Type and format validation - verify output is correct type and format
# 3. Cryptographic properties - verify key length and encoding
# 4. Randomness verification - ensure keys are unique
# 5. Consistency checks - verify function works reliably

# Standard Use Cases

def test_basic():
    """Test basic use case to ensure no syntax errors"""
    key = generate_symmetric_key()
    assert type(key) == str, "Generated key should be a string type"

def test_returns_string():
    """Test that function returns a string type"""
    key = generate_symmetric_key()
    assert isinstance(key, str), "Key returned is not a string type object"
    assert len(key) > 0, "Generated key should not be empty"

def test_key_length():
    """Test that generated key has correct length for base64-encoded 32 bytes"""
    key = generate_symmetric_key()
    # 32 bytes encoded in base64 should be 44 characters
    assert len(key) == 44, f"Expected key length of 44, got {len(key)}"

def test_valid_base64_encoding():
    """Test that generated key is valid base64 and decodes to 32 bytes"""
    key = generate_symmetric_key()
    try:
        decoded = base64.b64decode(key)
        assert len(decoded) == 32, f"Decoded key should be 32 bytes, got {len(decoded)}"
    except Exception as e:
        pytest.fail(f"Generated key is not valid base64: {e}")

def test_key_uniqueness():
    """Test that multiple calls generate different keys (randomness check)"""
    key1 = generate_symmetric_key()
    key2 = generate_symmetric_key()
    key3 = generate_symmetric_key()
    
    # All three keys should be different
    assert key1 != key2, "Keys should be unique"
    assert key2 != key3, "Keys should be unique"
    assert key1 != key3, "Keys should be unique"

def test_multiple_generation_consistency():
    """Test that function consistently returns valid keys across multiple calls"""
    for i in range(10):
        key = generate_symmetric_key()
        assert isinstance(key, str), f"Iteration {i}: key should be a string"
        assert len(key) == 44, f"Iteration {i}: key should have length 44"
        # Verify each key is valid base64
        decoded = base64.b64decode(key)
        assert len(decoded) == 32, f"Iteration {i}: decoded key should be 32 bytes"