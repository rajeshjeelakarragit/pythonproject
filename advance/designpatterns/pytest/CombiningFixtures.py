import pytest

@pytest.fixture
def fixture_one():
    return 1

@pytest.fixture
def fixture_two():
    return 2

def test_combined_fixtures(fixture_one, fixture_two):
    assert fixture_one + fixture_two == 3