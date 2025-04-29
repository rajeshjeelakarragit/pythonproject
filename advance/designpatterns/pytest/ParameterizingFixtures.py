import pytest
@pytest.fixture(params=["value1", "value2", "value3"])
def parameterized_fixture(request):
    return request.param

def test_with_parameters(parameterized_fixture):
    assert parameterized_fixture in ["value1", "value2", "value3"]
