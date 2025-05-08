import pytest

@pytest.fixture
def db_connection():
    # Simulate a database connection
    connection = {"status": "connected"}
    yield connection
    connection["status"] = "disconnected"

@pytest.fixture
def db_cursor(db_connection):
    # Use db_connection fixture
    db_connection["cursor"] = "cursor_ready"
    yield db_connection["cursor"]

def test_db_cursor(db_cursor):
    assert db_cursor == "cursor_ready"
