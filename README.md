# Welcome to imitation-game

[![Tests](https://github.com/UBC-MDS/imitation_game/actions/workflows/test.yml/badge.svg)](https://github.com/UBC-MDS/imitation_game/actions/workflows/test.yml)
[![Deploy](https://github.com/UBC-MDS/imitation_game/actions/workflows/release.yml/badge.svg)](https://github.com/UBC-MDS/imitation_game/actions/workflows/release.yml)
[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/downloads/)

`imitation-game` is a Python utility package for secure message processing. It provides a high-level interface for both Symmetric (shared secret) and Asymmetric (Public/Private key) encryption.

Symmetric Encryption
Fast and efficient encryption using a single shared key. Best for internal data storage or pre-shared secrets.

- generate_symmetric_key: Creates a cryptographically secure random key.
- encrypt_symmetric: Encrypts a plaintext message using a symmetric key.
- decrypt_symmetric: Restores an encrypted message back to plaintext using the same key.

Asymmetric Encryption (RSA)
Secure communication between two parties without needing to share a secret key beforehand. Uses sender/receiver key combinations where the sender encrypts with the receiver's public key AND signs with their own private key. This provides both confidentiality (only receiver can decrypt) and authenticity (receiver can verify the sender's identity), similar to PGP encryption.

- generate_asymmetric_key: Generates a pair of RSA keys: a Public Key (for encryption/verification) and a Private Key (for decryption/signing).
- encrypt_asymmetric: Encrypts a message using the receiver's public key and signs it with the sender's private key. Takes parameters: (message, receiver_public_key, sender_private_key).
- decrypt_asymmetric: Decrypts a message using the receiver's private key and verifies the sender's signature using the sender's public key. Takes parameters: (encrypted_data, receiver_private_key, sender_public_key).

## Comparison with the Python Ecosystem

There are many message encoding and decoding related packages on the PyPI server. We have selected a few key examples that with similar functionality as our package.

- [Cipher-symmetric](https://pypi.org/project/cipher-symmetric): Focuses exclusively on symmetric string encryption, acting as a high-level wrapper for the cryptography module.
- [Encryption](https://pypi.org/project/encryptions): A broad educational tool demonstrating AES, RSA, and hashing via `pycryptodome`. It is comprehensive but often requires more boilerplate code to implement.
- [encrypt_data](https://pypi.org/project/encrypt-data): Specializes in Hybrid Encryption, which uses asymmetric keys to securely exchange symmetric keys.

While the packages above are powerful, they often cater to either a single encryption style or require deep cryptographic knowledge to configure properly. The primary benefit of `imitation-game` is its focus on a unified, high-level API that abstracts away the complexity of both symmetric and asymmetric workflows.

## Installation

```bash
pip install imitation-game
```

**Dependencies:**
- `pycryptodome` - Cryptographic operations
- `pathvalidate` - File path validation

**Test PyPI**: <https://test.pypi.org/project/imitation_game>

## Usage Examples

### Symmetric Key Generation

```python
from imitation_game import generate_symmetric_key

# Generate a secure random key for symmetric encryption
key = generate_symmetric_key()
print(f"Generated key: {key[:10]}...")  # Shows first 10 characters

# Save the key to a file for later use
key = generate_symmetric_key("keys/my_encryption_key.txt")
```

### Symmetric Encryption

```python
from imitation_game import generate_symmetric_key, encrypt_symmetric, decrypt_symmetric

# Generate key 
key = generate_symmetric_key()

# Encrypts and decrypts message with key
message = "Secret message"
encrypted_data = encrypt_symmetric(message, key)
decrypted_message = decrypt_symmetric(encrypted_data, key)
print(decrypted_message)  # "Secret message"
```

### Asymmetric Encryption (Sender/Receiver)

```python
from imitation_game import generate_asymmetric_key, encrypt_asymmetric, decrypt_asymmetric

# Generate key pairs for sender and receiver
sender_private, sender_public = generate_asymmetric_key()
receiver_private, receiver_public = generate_asymmetric_key()

# Sender encrypts message with receiver's public key and signs with their private key
message = "Secret message"
encrypted_data = encrypt_asymmetric(message, receiver_public, sender_private)

# Receiver decrypts with their private key and verifies sender's signature
decrypted_message = decrypt_asymmetric(encrypted_data, receiver_private, sender_public)
print(decrypted_message)  # "Secret message"
```


## For Developers

If you want to contribute to this package or run it locally for development, here's what you need to know.

### Environment Setup

We use Hatch for managing the development environment. First, make sure you have Python 3.10 or higher installed.

Install Hatch:
```bash
pip install hatch
```

For conda users, we also provide an `environment.yml` file:
```bash
conda env create -f environment.yml
conda activate imitation_game
```

### Running Tests

To run the full test suite across all supported Python versions:
```bash
hatch run test:run
```

To run tests for a specific Python version:
```bash
hatch run test.py3.12:run
```

### Building Documentation

The documentation is built using Sphinx. To build it locally:
```bash
hatch run docs:build
```

To serve the docs locally and see changes in real-time:
```bash
hatch run docs:serve
```

### CI/CD Pipeline

We use GitHub Actions for continuous integration and deployment:
- **Tests**: Run automatically on every push and pull request
- **Release**: Automatically deploys to TestPyPI when changes are pushed to main
- **Docs**: Documentation is built and deployed on every push

## Contributing

For information about how to contribute to this package, please review our [Contributing document](https://github.com/UBC-MDS/imitation_game/blob/main/CONTRIBUTING.md). All contributors must abide by our [Code of Conduct](https://github.com/UBC-MDS/imitation_game/blob/main/CODE_OF_CONDUCT.md)

## License

This packages uses the MIT License, more information can be found [here](https://github.com/UBC-MDS/imitation_game/blob/main/LICENSE)

## Credits

This package `imitation-game` is created with [`passwordler`] (<https://github.com/UBC-MDS/passwordler>) and the [`pyOpenSci copier template`] (<https://github.com/pyOpenSci/pyos-package-template>)

## Contributors

- Vinay Valson
- Tirth Joshi
- Teem Kwong
- Alexander Wen
