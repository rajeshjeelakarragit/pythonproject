import pytest

#1
@pytest.fixture
def sample_data():
    # Setup code
    data = {"key": "value"}
    return data
#2
def test_sample_data(sample_data):
    assert sample_data["key"] == "value"