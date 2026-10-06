import sqlite3
import pytest
from auditoria import RegistroAuditoria

@pytest.fixture
def db_sesion():
    """Fixture que crea una BD SQLite en memoria y la limpia al finalizar."""
    # Setup: inicialización
    conexion = sqlite3.connect(":memory:")
    cursor = conexion.cursor()
    cursor.execute("""
        CREATE TABLE logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT NOT NULL,
            accion TEXT NOT NULL
        )
    """)
    conexion.commit()

    yield conexion  # Entrega la conexión activa al test

    # Teardown: limpieza garantizada
    conexion.close()

@pytest.fixture
def servicio_auditoria(db_sesion):
    """Fixture que inyecta la conexión efímera en la clase a probar."""
    return RegistroAuditoria(db_sesion)

def test_registro_evento_exitoso(servicio_auditoria):
    id_evento = servicio_auditoria.registrar_evento("admin", "LOGIN_SUCCESS")
    assert id_evento == 1

def test_aislamiento_de_datos(servicio_auditoria):
    # Demuestra que cada prueba inicia con una base de datos vacía e independiente
    eventos = servicio_auditoria.obtener_eventos_por_usuario("admin")
    assert len(eventos) == 0

def test_consulta_multiples_eventos(servicio_auditoria):
    servicio_auditoria.registrar_evento("jperez", "CONSULTA_SALDO")
    servicio_auditoria.registrar_evento("jperez", "TRANSFERENCIA")
    
    eventos = servicio_auditoria.obtener_eventos_por_usuario("jperez")
    assert len(eventos) == 2
    assert "TRANSFERENCIA" in eventos