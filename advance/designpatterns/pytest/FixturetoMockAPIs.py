from unittest.mock import MagicMock
import pytest

@pytest.fixture
def mock_api():
    api = MagicMock()
    api.get_data.return_value = {"key": "mocked_value"}
    return api

def test_mock_api(mock_api):
    response = mock_api.get_data()
    assert response["key"] == "mocked_value"
