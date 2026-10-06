import pytest

@pytest.mark.parametrize(
    "numero, esperado",
    [
        (2, True),
        (4, True),
        (7, False),
        (9, False),
        (0, True)
    ]
)
def test_es_par(numero, esperado):
    assert es_par(numero) == esperado