"""Tests for encrypt_symmetric function."""
from imitation_game.encrypt_symmetric import encrypt_symmetric

def test_encrypt_symmetric_basic():
    """Test file present"""
    key = "524"
    plaintext = "hello world"
    ciphertext = b'\x1e7~\xc6\x85{x\x8a\xd2=\xca'
    expected = ciphertext
    actual = encrypt_symmetric(plaintext, key)
    assert actual == expected