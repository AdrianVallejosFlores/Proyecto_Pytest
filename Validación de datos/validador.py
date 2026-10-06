import re

def validar_registro_usuario(username: str, edad: int, email: str) -> bool:
    if not isinstance(username, str) or not (3 <= len(username.strip()) <= 20):
        raise ValueError("El nombre de usuario debe tener entre 3 y 20 caracteres.")
    
    if not isinstance(edad, int) or edad < 18 or edad > 100:
        raise ValueError("La edad debe ser un número entero entre 18 y 100 años.")
    
    patron_email = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if not isinstance(email, str) or not re.match(patron_email, email):
        raise ValueError("El formato del correo electrónico es inválido.")
    
    return True