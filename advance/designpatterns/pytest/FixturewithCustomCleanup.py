import pytest

@pytest.fixture
def temp_file(request):
    file = open("temp.txt", "w")
    file.write("Temporary file content")
    file.close()

    def cleanup():
        import os
        os.remove("temp.txt")

    request.addfinalizer(cleanup)
    return "temp.txt"

def test_temp_file(temp_file):
    assert temp_file == "temp.txt"
