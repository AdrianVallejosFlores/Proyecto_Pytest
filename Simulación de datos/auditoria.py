import sqlite3

class RegistroAuditoria:
    def __init__(self, conexion):
        self.conexion = conexion

    def registrar_evento(self, usuario: str, accion: str) -> int:
        cursor = self.conexion.cursor()
        cursor.execute(
            "INSERT INTO logs (usuario, accion) VALUES (?, ?)",
            (usuario, accion)
        )
        self.conexion.commit()
        return cursor.lastrowid

    def obtener_eventos_por_usuario(self, usuario: str) -> list:
        cursor = self.conexion.cursor()
        cursor.execute(
            "SELECT accion FROM logs WHERE usuario = ?",
            (usuario,)
        )
        return [fila[0] for fila in cursor.fetchall()]