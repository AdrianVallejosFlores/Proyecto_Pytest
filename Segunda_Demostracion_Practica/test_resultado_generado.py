import pytest
from notas import calcular_promedio, asignar_calificacion, esta_aprobado


# ---------- calcular_promedio ----------

# Verifica el promedio en casos válidos
@pytest.mark.parametrize("notas, esperado", [
    ([80, 90, 100], 90),    # promedio normal
    ([85], 85),             # una sola nota
    ([0, 0, 0], 0),         # todas las notas en cero
    ([60, 75], 67.5),       # resultado decimal
])
def test_promedio_valido(notas, esperado):
    assert calcular_promedio(notas) == pytest.approx(esperado)


# Verifica que lista vacía, nota negativa o nota mayor a 100 lancen ValueError
@pytest.mark.parametrize("notas", [
    [],
    [80, -5, 90],
    [80, 105, 90],
])
def test_promedio_invalido(notas):
    with pytest.raises(ValueError):
        calcular_promedio(notas)


# ---------- asignar_calificacion ----------

# Verifica cada letra, incluyendo los valores límite entre rangos
@pytest.mark.parametrize("nota, esperada", [
    (100, "A"), (90, "A"),
    (89, "B"), (80, "B"),
    (79, "C"), (70, "C"),
    (69, "D"), (60, "D"),
    (59, "F"), (0, "F"),
])
def test_asignar_calificacion(nota, esperada):
    assert asignar_calificacion(nota) == esperada


# Verifica que notas fuera de rango lancen ValueError
@pytest.mark.parametrize("nota", [-1, 101])
def test_calificacion_fuera_de_rango(nota):
    with pytest.raises(ValueError):
        asignar_calificacion(nota)


# ---------- esta_aprobado ----------

# Verifica la aprobación con el mínimo por defecto y con uno personalizado
@pytest.mark.parametrize("notas, minimo, esperado", [
    ([70, 80, 90], 60, True),    # por encima del mínimo
    ([60, 60], 60, True),        # justo en el mínimo
    ([50, 55], 60, False),       # por debajo del mínimo
    ([70, 80], 80, False),       # mínimo personalizado, no alcanzado
    ([80, 80], 80, True),        # mínimo personalizado, alcanzado
])
def test_esta_aprobado(notas, minimo, esperado):
    assert esta_aprobado(notas, minimo) == esperado


# Verifica que una lista vacía propague el error de calcular_promedio
def test_esta_aprobado_lista_vacia():
    with pytest.raises(ValueError):
        esta_aprobado([])