"""Tests for generate_symmetric_key function."""
from imitation_game.generate_symmetric_key import generate_symmetric_key
import pytest
import base64

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