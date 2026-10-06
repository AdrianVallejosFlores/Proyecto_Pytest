import pytest
from promedio import calcular_promedio


# Verifica el promedio en casos válidos con distintas listas de notas
@pytest.mark.parametrize("notas, esperado", [
    ([80, 90, 100], 90),     # promedio normal
    ([85], 85),              # una sola nota
    ([0, 0, 0], 0),          # todas las notas en cero
    ([60, 75], 67.5),        # resultado decimal
])
def test_promedio_valido(notas, esperado):
    assert calcular_promedio(notas) == pytest.approx(esperado)


# Verifica que una lista vacía lance ValueError
def test_lista_vacia():
    with pytest.raises(ValueError):
        calcular_promedio([])


# Verifica que una nota negativa lance ValueError
def test_nota_negativa():
    with pytest.raises(ValueError):
        calcular_promedio([80, -5, 90])


# Verifica que una nota superior a 100 lance ValueError
def test_nota_superior_a_cien():
    with pytest.raises(ValueError):
        calcular_promedio([80, 105, 90])