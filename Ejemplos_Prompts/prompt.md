Actúa como desarrollador especializado en testing de software con Python.
Genera pruebas automatizadas con pytest para la siguiente función:

def calcular_promedio(notas):
    if not notas:
        raise ValueError("La lista no puede estar vacía")
    for nota in notas:
        if nota < 0 or nota > 100:
            raise ValueError("Nota fuera de rango")
    return sum(notas) / len(notas)