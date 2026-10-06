import pytest

from calculadora import calcular_descuento


@pytest.mark.parametrize(
	("precio", "porcentaje", "esperado"),
	[
		(100, 0, 100),  # El 0 % mantiene el precio original.
		(100, 10, 90),  # El 10 % descuenta correctamente una parte del precio.
		(100, 100, 0),  # El 100 % deja el precio final en cero.
		(0, 10, 0),     # Un precio cero produce un resultado cero.
	],
)
def test_calcular_descuento_casos_validos(precio, porcentaje, esperado):
	"""Verifica los resultados de descuentos y precios válidos."""
	assert calcular_descuento(precio, porcentaje) == pytest.approx(esperado)


def test_calcular_descuento_rechaza_precio_negativo():
	"""Verifica que un precio negativo genera ValueError."""
	with pytest.raises(ValueError):
		calcular_descuento(-1, 10)


@pytest.mark.parametrize("porcentaje", [-1, 101])
def test_calcular_descuento_rechaza_porcentaje_fuera_de_rango(porcentaje):
	"""Verifica que se rechazan porcentajes inferiores a 0 o superiores a 100."""
	with pytest.raises(ValueError):
		calcular_descuento(100, porcentaje)
