# Welcome to imitation-game

This package provides message encoding and decoding tools in Python. The package consists of five functions:
- encode_data: The primary encoder. It rotates each letter of the alphabet forward based on a numerical shift value while preserving original casing and non-alphabetic characters.
- decode_data: The inverse of the encoder. It processes an encoded string using the corresponding shift value to restore the original human-readable message.
- generate_shift: A utility function that generates a random integer (1–25). This ensures that every session can utilize a unique, non-static encryption key.
- encrypt_shift: A security wrapper for the shift key. Instead of exposing the raw integer used for rotation, this function encrypts the key to prevent casual observers from identifying the cipher pattern.
- decrypt_shift: The retrieval function for the shift key. It restores the encrypted key to its original integer form, enabling the decode_data function to operate accurately.

## Comparison with the Python Ecosystem
There are many message encoding and decoding related packages on the PyPI server. We have selected a few key examples that with similar functionality as our package.

- [Caesar Cipher CLI Tool](https://pypi.org/project/caesar-cipher-cli): encrypt and decrypt text using the Caesar cipher algorithm.
- [Vigener_Coder_n_Decoder](https://pypi.org/project/viegenere-message-encoder-GameDevNoOne): encodes and decodes Viegener codes.
- [Cryptography Library](https://pypi.org/project/CryptoC): provides a collection of ciphers that you can use to encrypt and decrypt data.

However, there is no package that encrypt and decrypt the key. The primary benefit of imitation-game is its integrated key management. By providing dedicated functions to generate and encrypt the shift key, we provide a more comprehensive "end-to-end" simulation of the encryption process, ensuring the key is just as protected as the message.

## Installation

```bash
$ pip install imitation-game
```

## Contributing 
For information about how to contribute to this package, please review our [Contributing document](https://github.com/alxwen711/imitation_game/blob/main/CONTRIBUTING.md). All contributors must abide by our [Code of Conduct](https://github.com/alxwen711/imitation_game/blob/main/CODE_OF_CONDUCT.md)

## License
This packages uses the MIT License, more information can be found [here](https://github.com/alxwen711/imitation_game/blob/main/LICENSE)

## Credits
This package `imitation-game` is created with [`passwordler`] (https://github.com/UBC-MDS/passwordler) and the [`pyOpenSci copier template`] (https://github.com/pyOpenSci/pyos-package-template)

## Contributors
- Vinay Valson
- Tirth Joshi
- Teem Kwong
- Alexander Wen
