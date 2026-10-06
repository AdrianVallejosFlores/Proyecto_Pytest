def calcular_promedio(notas):
    if not notas:
        raise ValueError("La lista no puede estar vacía")

    for nota in notas:
        if nota < 0 or nota > 100:
            raise ValueError("Nota fuera de rango")

    return sum(notas) / len(notas)


def asignar_calificacion(nota):
    if nota < 0 or nota > 100:
        raise ValueError("Nota fuera de rango")

    # PARA LA PRUEBA FALLIDA PODEMOS QUITA EL '=' EN LOS IFs PARA QUE NO INCLUYA EL LÍMITE SUPERIOR
    if nota >= 90:
        return "A"
    if nota >= 80:
        return "B"
    if nota >= 70:
        return "C"
    if nota >= 60:
        return "D"
    return "F"


def esta_aprobado(notas, minimo=60):
    return calcular_promedio(notas) >= minimo