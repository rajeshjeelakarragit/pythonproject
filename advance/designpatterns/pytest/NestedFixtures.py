import pytest

@pytest.fixture
def base_config():
    return {"url": "http://example.com"}

@pytest.fixture
def extended_config(base_config):
    base_config["timeout"] = 30
    return base_config

def test_config(extended_config):
    assert extended_config["url"] == "http://example.com"
    assert extended_config["timeout"] == 30
