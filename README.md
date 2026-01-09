# Welcome to imitation-game

`imitation-game` is a Python utility package for secure message processing. It provides a high-level interface for both Symmetric (shared secret) and Asymmetric (Public/Private key) encryption.

Symmetric Encryption
Fast and efficient encryption using a single shared key. Best for internal data storage or pre-shared secrets.
- generate_symmetric_key: Creates a cryptographically secure random key.
- encrypt_symmetric: Encrypts a plaintext message using a symmetric key.
- decrypt_symmetric: Restores an encrypted message back to plaintext using the same key.

Asymmetric Encryption (RSA)
Secure communication between two parties without needing to share a secret key beforehand.
- generate_asymmetric_key: Generates a pair of RSA keys: a Public Key (for encryption) and a Private Key (for decryption).
- encrypt_asymmetric: Encrypts a message using a public key.
- decrypt_asymmetric: Decrypts a message using the corresponding private key.

## Comparison with the Python Ecosystem
There are many message encoding and decoding related packages on the PyPI server. We have selected a few key examples that with similar functionality as our package.

- [Cipher-symmetric](https://pypi.org/project/cipher-symmetric): Focuses exclusively on symmetric string encryption, acting as a high-level wrapper for the cryptography module.
- [Encryption](https://pypi.org/project/encryptions): A broad educational tool demonstrating AES, RSA, and hashing via `pycryptodome`. It is comprehensive but often requires more boilerplate code to implement.
- [encrypt_data](https://pypi.org/project/encrypt-data): Specializes in Hybrid Encryption, which uses asymmetric keys to securely exchange symmetric keys.

While the packages above are powerful, they often cater to either a single encryption style or require deep cryptographic knowledge to configure properly. The primary benefit of `imitation-game` is its focus on a unified, high-level API that abstracts away the complexity of both symmetric and asymmetric workflows.

## Installation

```bash
$ pip install imitation-game
```

## Contributing 
For information about how to contribute to this package, please review our [Contributing document](https://github.com/UBC-MDS/imitation_game/blob/main/CONTRIBUTING.md). All contributors must abide by our [Code of Conduct](https://github.com/UBC-MDS/imitation_game/blob/main/CODE_OF_CONDUCT.md)

## License
This packages uses the MIT License, more information can be found [here](https://github.com/UBC-MDS/imitation_game/blob/main/LICENSE)

## Credits
This package `imitation-game` is created with [`passwordler`] (https://github.com/UBC-MDS/passwordler) and the [`pyOpenSci copier template`] (https://github.com/pyOpenSci/pyos-package-template)

## Contributors
- Vinay Valson
- Tirth Joshi
- Teem Kwong
- Alexander Wen
