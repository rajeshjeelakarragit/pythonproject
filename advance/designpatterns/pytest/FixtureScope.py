"""
Fixtures can have different scopes:

function (default): A new instance is created for each test function.
class: One instance is created per test class.
module: One instance is created per test module.
session: One instance is created per testing session.

"""
import pytest
@pytest.fixture(scope="module")
def setup_database():
    # Setup code for database
    db = {"connection": "connected"}
    yield db
    # Teardown code
    db["connection"] = "disconnected"

@pytest.fixture
def resource():
    # Setup code
    res = "Resource setup"
    yield res
    # Teardown code
    print("Resource teardown")


@pytest.fixture(scope="class")
def shared_resource():
    return {"key": "shared_value"}

class TestClassExample:
    def test_one(self, shared_resource):
        assert shared_resource["key"] == "shared_value"

    def test_two(self, shared_resource):
        assert shared_resource["key"] == "shared_value"