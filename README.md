# Welcome to imitation-game

[![CI](https://github.com/UBC-MDS/imitation_game/actions/workflows/build.yml/badge.svg)](https://github.com/UBC-MDS/imitation_game/actions/workflows/build.yml)
[![CD](https://github.com/UBC-MDS/imitation_game/actions/workflows/deploy.yml/badge.svg)](https://github.com/UBC-MDS/imitation_game/actions/workflows/deploy.yml)
[![Docs](https://github.com/UBC-MDS/imitation_game/actions/workflows/docs.yml/badge.svg)](https://github.com/UBC-MDS/imitation_game/actions/workflows/docs.yml)
[![codecov](https://codecov.io/gh/UBC-MDS/imitation_game/branch/main/graph/badge.svg)](https://codecov.io/gh/UBC-MDS/imitation_game)
[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/downloads/)
[![Package Version](https://img.shields.io/badge/version-0.2.2-blue)](https://test.pypi.org/project/imitation-game/)


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



## Development

### Setting Up the Development Environment

This project uses conda for environment management, but dependencies are defined in `pyproject.toml`. Follow these steps to set up your development environment:

1. **Create a conda environment** with Python 3.10 or higher:
   ```bash
   conda create -n imitation-game python=3.12
   conda activate imitation-game
   ```
   
   Alternatively, use the provided `environment.yml` file:
   ```bash
   conda env create -f environment.yml
   conda activate imitation_game
   ```

2. **Install the package in editable mode** with all development dependencies:
   ```bash
   # Clone the repository
   git clone https://github.com/UBC-MDS/imitation_game.git
   cd imitation_game
   
   # Install the package with all optional dependencies (dev, docs, tests, build)
   pip install -e ".[dev,docs,tests,build]"
   ```

   This will install:
   - The package itself in editable mode
   - Development tools: `hatch`, `pre-commit`
   - Documentation tools: `quartodoc`
   - Testing tools: `pytest`, `pytest-cov`, `pytest-raises`, `pytest-randomly`, `pytest-xdist`, `flake8-pyproject`
   - Build tools: `pip-audit`, `twine`

### Running Tests

Tests are located in the `tests/` directory and can be run using pytest:

```bash
# Run all tests
pytest

# Run tests with coverage report
pytest --cov=imitation_game --cov-report=term-missing

# Run tests using hatch (recommended)
hatch run +py=3.12 test:run
```


The test suite includes both unit tests (`tests/unit/`) and integration tests (`tests/integration/`).

### Building Documentation

Documentation is built using Quarto and quartodoc. To build the documentation locally:

1. **Ensure Quarto is installed**:
   - Download and install Quarto from [https://quarto.org/docs/get-started/](https://quarto.org/docs/get-started/)

2. **Build the documentation**:
   ```bash
   # Generate API reference documentation
   quartodoc build
   
   # Render the Quarto website
   quarto render
   ```

3. **Preview the documentation locally**:
   ```bash
   quarto preview
   ```

The documentation will be generated in the `_site/` directory (or similar, depending on your Quarto configuration).

### Automated Documentation Deployment

Documentation is automatically built and deployed to GitHub Pages when:
- Changes are pushed to the `main` branch
- The workflow is manually triggered via GitHub Actions

The deployment workflow (`.github/workflows/docs.yml`) handles:
- Building the Quarto documentation
- Publishing to the `gh-pages` branch
- Making the documentation available at the repository's GitHub Pages URL

No manual intervention is required for documentation deployment once changes are merged to `main`.
Documentation is deployed [here](https://ubc-mds.github.io/imitation_game/)

### CI/CD Pipeline

We use GitHub Actions for continuous integration and deployment:
- **Tests**: Run automatically on every push and pull request via `build.yml`
- **Deploy**: Automatically deploys to TestPyPI when changes are pushed to main via `deploy.yml`
- **Docs**: Documentation is built and deployed to GitHub Pages on every push via `docs.yml`


## Contributing

For information about how to contribute to this package, please review our [Contributing document](https://github.com/UBC-MDS/imitation_game/blob/main/CONTRIBUTING.md). All contributors must abide by our [Code of Conduct](https://github.com/UBC-MDS/imitation_game/blob/main/CODE_OF_CONDUCT.md)

## License

This packages uses the MIT License, more information can be found [here](https://github.com/UBC-MDS/imitation_game/blob/main/LICENSE)

## Credits

This package `imitation-game` is created with [`pyOpenSci copier template`] (<https://github.com/pyOpenSci/pyos-package-template>)

## Contributors

### Vinay Valson

- **Affiliation**: University of British Columbia
- **GitHub**: [@Vin-dictive](https://github.com/Vin-dictive)

### Tirth Joshi

- **Affiliation**: University of British Columbia
- **GitHub**: [@tirthjoship](https://github.com/tirthjoship)

### Teem Kwong

- **Affiliation**: University of British Columbia
- **GitHub**: [@mdskwong](https://github.com/mdskwong)

### Alexander Wen

- **Affiliation**: University of British Columbia
- **GitHub**: [@alxwen711](https://github.com/alxwen711)
