import pytest
from validador import validar_registro_usuario

def test_registro_usuario_valido():
    # Caso válido que cumple todos los criterios
    resultado = validar_registro_usuario("carlos_v", 24, "carlos@example.com")
    assert resultado is True

def test_username_demasiado_corto():
    # Verifica que lance ValueError con mensaje específico
    with pytest.raises(ValueError, match="El nombre de usuario debe tener entre 3 y 20 caracteres."):
        validar_registro_usuario("ab", 25, "user@test.com")

def test_edad_menor_de_edad():
    with pytest.raises(ValueError, match="La edad debe ser un número entero entre 18 y 100 años."):
        validar_registro_usuario("esteban", 17, "esteban@test.com")

@pytest.mark.parametrize("email_invalido", [
    "sin_arroba.com",
    "usuario@",
    "@dominio.com",
    "usuario@dominio",
    "",
])
def test_correos_con_formato_incorrecto(email_invalido):
    # Se evalúan 5 variantes de correos inválidos con una sola función
    with pytest.raises(ValueError, match="El formato del correo electrónico es inválido."):
        validar_registro_usuario("usuarioValido", 30, email_invalido)