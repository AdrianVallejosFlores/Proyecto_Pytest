def calcular_descuento(precio, porcentaje): 
    if precio < 0: raise ValueError("El precio no puede ser negativo") 
    if porcentaje < 0 or porcentaje > 100: raise ValueError("El porcentaje debe estar entre 0 y 100") 
    return precio - (precio * porcentaje / 100)