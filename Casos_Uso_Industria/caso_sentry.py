import pytest

@pytest.fixture
def evento_error():
    return {"mensaje": "ZeroDivisionError", "nivel": "error"}

def test_evento_tiene_nivel_error(evento_error):
    assert evento_error["nivel"] == "error"