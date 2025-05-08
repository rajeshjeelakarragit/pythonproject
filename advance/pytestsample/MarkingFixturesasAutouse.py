import pytest

@pytest.fixture(autouse=True)
def auto_fixture():
    print("This runs before every test")


@pytest.fixture(autouse=True)
def log_test():
    print("\nTest is starting...")

def test_example_one():
    assert 1 + 1 == 2

def test_example_two():
    assert "pytestsample".upper() == "PYTEST"