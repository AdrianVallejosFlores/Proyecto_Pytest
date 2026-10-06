Actúa como un desarrollador especializado en testing de software con Python.
Genera pruebas automatizadas con pytest para las funciones calcular_promedio,
asignar_calificacion y esta_aprobado del módulo notas.py.

Las pruebas deben cubrir casos normales, casos límite y casos de error:
- calcular_promedio: un promedio normal, una sola nota, todas las notas en 0,
  un resultado decimal, una lista vacía, una nota negativa y una nota mayor a 100.
- asignar_calificacion: los límites de cada letra (90, 89, 80, 79, 70, 69, 60, 59),
  los extremos 0 y 100, y notas fuera de rango (-1 y 101).
- esta_aprobado: promedio igual al mínimo, por encima, por debajo, un mínimo
  personalizado y una lista vacía.

Utiliza assert para comprobar los resultados, pytest.raises para las excepciones,
pytest.mark.parametrize para los casos similares y pytest.approx al comparar
decimales. Agrega un comentario breve en cada prueba explicando qué verifica.
Devuelve únicamente el código, listo para guardar como test_notas.py.


(pasar el codigo de notas.py)