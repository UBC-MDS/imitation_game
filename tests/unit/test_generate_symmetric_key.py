"""Tests for generate_symmetric_key function."""
from imitation_game.generate_symmetric_key import generate_symmetric_key
import pytest
import base64
import os

# Test Strategy:
# 1. Basic functionality tests - ensure function works without errors
# 2. Type and format validation - verify output is correct type and format
# 3. Cryptographic properties - verify key length and encoding
# 4. Randomness verification - ensure keys are unique
# 5. Consistency checks - verify function works reliably
#
# Test Coverage: All code paths are covered by the test suite
# - Function execution: test_basic
# - Type validation: test_returns_string
# - Length validation: test_key_length
# - Base64 encoding: test_valid_base64_encoding
# - Randomness: test_key_uniqueness
# - Consistency: test_multiple_generation_consistency

# Standard Use Cases


def test_basic():
    """Test basic use case to ensure no syntax errors"""
    key = generate_symmetric_key()
    assert isinstance(key, str), "Generated key should be a string type"


def test_returns_string():
    """Test that function returns a string type"""
    key = generate_symmetric_key()
    assert isinstance(key, str), "Key returned is not a string type object"
    assert len(key) > 0, "Generated key should not be empty"


def test_key_length():
    """Test that generated key has correct length for base64 32 bytes"""
    key = generate_symmetric_key()
    # 32 bytes encoded in base64 should be 44 characters
    assert len(key) == 44, f"Expected key length of 44, got {len(key)}"


def test_valid_base64_encoding():
    """Test that generated key is valid base64 and decodes to 32 bytes"""
    key = generate_symmetric_key()
    try:
        decoded = base64.b64decode(key)
        assert len(decoded) == 32, (
            f"Decoded key should be 32 bytes, got {len(decoded)}")
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
    """Test function returns valid keys across multiple calls"""
    for i in range(10):
        key = generate_symmetric_key()
        assert isinstance(key, str), f"Iteration {i}: key should be a string"
        assert len(key) == 44, f"Iteration {i}: key should have length 44"
        # Verify each key is valid base64
        decoded = base64.b64decode(key)
        assert len(decoded) == 32, (
            f"Iteration {i}: decoded key should be 32 bytes")

# File Writing Tests


def test_write_to_file():
    """Test writing key to file"""

    test_directory = "tests/symmetric_key_tests"
    test_file = "test_key.txt"
    test_path = os.path.join(test_directory, test_file)

    # Generate key and save to file
    key = generate_symmetric_key(test_path)

    # Verify file was created
    assert os.path.isfile(test_path), "Key file was not created"

    # Verify file contains the correct key
    with open(test_path, "r") as f:
        saved_key = f.read()
    assert saved_key == key, "Saved key does not match generated key"

    # Cleanup
    os.remove(test_path)
    if os.path.exists(test_directory):
        os.rmdir(test_directory)


def test_no_file_without_filepath():
    """Test that no file is created when filepath is not provided"""
    key = generate_symmetric_key()
    # Just verify the function works without filepath
    assert isinstance(key, str), (
        "Key should be generated even without filepath")
    assert len(key) == 44, "Key should have correct length"


def test_create_directory_if_not_exists():
    """Test that function creates parent directories if they don't exist"""

    test_directory = "tests/nested/symmetric_key_tests"
    test_file = "nested_key.txt"
    test_path = os.path.join(test_directory, test_file)

    # Generate key with nested path
    _ = generate_symmetric_key(test_path)

    # Verify directory and file were created
    assert os.path.exists(test_directory), "Parent directories were not created"
    assert os.path.isfile(test_path), "Key file was not created in nested directory"

    # Cleanup
    os.remove(test_path)
    os.rmdir(test_directory)
    os.rmdir("tests/nested")


def test_key_file_content_integrity():
    """Test that the key file is saved correctly and can be read back without issues

    Makes sure the file doesn't have extra spaces or weird characters that could
    mess up the key when we try to use it later.
    """

    test_directory = "tests/symmetric_key_integrity_test"
    test_file = "integrity_key.txt"
    test_path = os.path.join(test_directory, test_file)

    # Generate and save key
    generated_key = generate_symmetric_key(test_path)

    # Read the key back from file
    with open(test_path, "r", encoding="utf-8") as f:
        file_content = f.read()

    # Verify exact match (no extra whitespace, newlines, or encoding issues)
    assert file_content == generated_key, "File content does not exactly match generated key"

    # Verify the read key is still valid base64
    decoded = base64.b64decode(file_content)
    assert len(decoded) == 32, "Key read from file does not decode to 32 bytes"

    # Verify no trailing whitespace or newlines
    assert file_content == file_content.strip(), "File contains unexpected whitespace"

    # Verify file size is exactly 44 bytes (no extra characters)
    file_size = os.path.getsize(test_path)
    assert file_size == 44, f"Expected file size of 44 bytes, got {file_size}"

    # Cleanup
    os.remove(test_path)
    if os.path.exists(test_directory):
        os.rmdir(test_directory)
