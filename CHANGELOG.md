# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Added badges for CICD, TestPyPi, and documentation



## [0.0.3] - (2026-01-25)

### Added

- Type hints for encrypt_asymmetric and decrypt_asymmetric functions
- Documentation comments in test files listing all LLM-suggested tests
- Added PGP style encryption function and tests
- Developer documentation section in README with setup and workflow instructions
- CI/CD status badges to README
- Conda environment.yml file for easier setup
- File integrity test for generate_symmetric_key
- Filepath validation in generate_symmetric_key for better error handling
- Automated documentation generation (#62)
- Example use case and unit test for generate_asymmetric_key (#64)

### Changed

- Updated parameter types in encrypt_asymmetric
- Updated parameter types in decrypt_asymmetric
- Updated docstrings to reflect correct parameter types (bytes instead of str)

## [0.0.2] - (2026-01-17)

### Added
- Implementation of symmetric encryption functions: generate_symmetric_key, encrypt_symmetric, decrypt_symmetric (#21 #30 #35 #39)
- Implementation of asymmetric encryption functions: generate_asymmetric_key, encrypt_asymmetric, decrypt_asymmetric (#26 #27 #29 #31 #32)
- Added pathvalidate dependency for file path validation (#36)
- Added key file support for symmetric encryption and decryption (#39)
- Complete README with usage examples for all functions (#36)
- Comprehensive test suite with 55 tests covering all functions

## [0.1.0] - (2026-01-10)

- CONTRIBUTING.md, add feature request template #9
- README.md and function docstrings #10 #14
- CODE_OF_CONDUCT.md #15
- Fix GitHub workflow #17

[0.0.2]: https://github.com/UBC-MDS/imitation_game/compare/0.1.0...0.0.2
[0.1.0]: https://github.com/UBC-MDS/imitation_game/releases/tag/0.1.0
