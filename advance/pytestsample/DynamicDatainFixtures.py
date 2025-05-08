import random
import pytest

@pytest.fixture
def random_number():
    return random.randint(1, 100)

def test_random_number(random_number):
    assert 1 <= random_number <= 100
