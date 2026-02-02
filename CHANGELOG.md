# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

<!--versionlist-->

## v1.1.2 (2026-02-02)

### Bug Fixes

- Improve asymmetric error handling implementation
  ([`ef15f79`](https://github.com/UBC-MDS/imitation_game/commit/ef15f79a5af75a97c6702931f074fc0daa483b51))

### Chores

- Fix flake8 linting errors in tests
  ([`f6f5d1d`](https://github.com/UBC-MDS/imitation_game/commit/f6f5d1d8bcb8af4d7ee67f8a625d99b3d998527b))

### Documentation

- Add expected output to README use cases
  ([`a61c34b`](https://github.com/UBC-MDS/imitation_game/commit/a61c34b047c58d35cabc4f2916c8a6b815f2f165))

- Add flake8 and black to tools reflection
  ([`29f58a4`](https://github.com/UBC-MDS/imitation_game/commit/29f58a4b997681aa990cb8e4870cb37eb6d73776))

- Add infrastructure and practices sections to reflection
  ([`86ec522`](https://github.com/UBC-MDS/imitation_game/commit/86ec522b0482b5b6dfe980179cd991f11687da95))

- Add initial reflection page describing our tools
  ([`221b31a`](https://github.com/UBC-MDS/imitation_game/commit/221b31ab22011a69e9fdd3ec9c4ed034c199b017))

- Add reflection page to website navbar
  ([`dde177b`](https://github.com/UBC-MDS/imitation_game/commit/dde177b47384af1b0c04ed0ac145d41cb7c4f3b7))

- Add scalability and future improvements to reflection
  ([`6720c96`](https://github.com/UBC-MDS/imitation_game/commit/6720c96a2a0b4d978c9479a5027c2d6b2cd19c00))

### Testing

- Add explicit edge case tests
  ([`2030b4d`](https://github.com/UBC-MDS/imitation_game/commit/2030b4d158bf2a5b0986c94bbd109564f72a4e36))

- Update unit tests for detailed assert messages
  ([`a73f547`](https://github.com/UBC-MDS/imitation_game/commit/a73f547eede3fdd4c8646190e4076783b6becbfe))


## v1.1.1 (2026-01-31)

### Bug Fixes

- Correct broken project URLs and enhance installation docs
  ([`eafd9c6`](https://github.com/UBC-MDS/imitation_game/commit/eafd9c60fb0b19dc601ae8536a27a63d8eba92ef))

- Remove trailing dot from conftest.py link causing 404 error
  ([`45cb1d9`](https://github.com/UBC-MDS/imitation_game/commit/45cb1d93fbd7cea748e86867e72bbc16dab6a3f8))

### Documentation

- Add expected output examples to usage demonstrations
  ([`e6065eb`](https://github.com/UBC-MDS/imitation_game/commit/e6065ebee8535ce793b6b6c3bff39dbdf8fcea26))


## v1.1.0 (2026-01-31)

### Features

- Add changelog configuration for semantic release in pyproject.toml
  ([`4a201ef`](https://github.com/UBC-MDS/imitation_game/commit/4a201efcb966ae275f09605fa70199fbdd9f21e6))


### Added

- Added badges for CICD, TestPyPi, and documentation
- Cleaned up codebase to be compliant with flake8


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
