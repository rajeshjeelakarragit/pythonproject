import pytest

def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="dev", help="Environment to run tests in")

@pytest.fixture
def environment(request):
    return request.config.getoption("--env")

def test_environment(environment):
    assert environment in ["dev", "staging", "prod"]

"""
pytestsample --env=staging
"""