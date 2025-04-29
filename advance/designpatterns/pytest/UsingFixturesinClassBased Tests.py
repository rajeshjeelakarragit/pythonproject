
import pytest
class TestClass:
    @pytest.fixture
    def setup_class(self):
        return {"class_key": "class_value"}

    def test_class_fixture(self, setup_class):
        assert setup_class["class_key"] == "class_value"