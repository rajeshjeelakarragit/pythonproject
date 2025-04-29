# conftest.py
import pytest

@pytest.fixture
def global_fixture():
    return "Global Fixture"


# test_sample.py
def test_using_global(global_fixture):
    assert global_fixture == "Global Fixture"
