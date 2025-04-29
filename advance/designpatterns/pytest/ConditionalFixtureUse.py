import pytest

@pytest.fixture
def special_setup():
    print("\nSpecial setup is running")

@pytest.mark.usefixtures("special_setup")
def test_with_fixture():
    assert True
