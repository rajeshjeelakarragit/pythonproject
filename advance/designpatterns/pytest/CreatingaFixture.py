import pytest

@pytest.fixture
def sample_data():
    # Setup code
    data = {"key": "value"}
    return data

def test_sample_data(sample_data):
    assert sample_data["key"] == "value"