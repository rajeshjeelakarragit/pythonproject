import pytest

@pytest.fixture
def file_handler():
    # Setup
    file = open("test_file.txt", "w")
    file.write("Hello, pytestsample!")
    yield file
    # Teardown
    file.close()

def test_file_handler(file_handler):
    file_handler.seek(0)
    content = file_handler.read()
    assert content == "Hello, pytestsample!"
