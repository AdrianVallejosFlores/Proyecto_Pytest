import pytest

@pytest.mark.parametrize("entrada, esperado", [
    ("1+1", 2),
    ("2*3", 6),
    ("10-4", 6),
])
def test_evaluar_expresion(entrada, esperado):
    assert eval(entrada) == esperado