import pytest
import shutil

# Test cleanup code is adapted from
# https://github.com/ttimbers/breast-cancer-predictor/blob/3.0.0/tests/conftest.py


@pytest.fixture(autouse=True, scope="session")
def remove_testdata_directory():
    # This code will run at the end of the pytest session
    yield

    folders = ["tests/asymmetric_key_tests", "tests/asymmetric_integration"]
    for f in folders:
        try:
            shutil.rmtree(f)
        except FileNotFoundError:
            print(f"{f} does not exist")
            pass  # Directory doesn't exist, continue
