from conexionBD import conexion_bd
from datetime import datetime

class Nota:
    def __init__(self):
        self.conexion = conexion_bd.get_conexion()
        self.cursor = conexion_bd.get_cursor()
    
    def crear(self, usuario_id: int, titulo: str, descripcion: str) -> bool:
        try:
            if not usuario_id or not titulo.strip():
                return False
                
            sql = """
                INSERT INTO notas 
                (usuario_id, titulo, descripcion, fecha) 
                VALUES (%s, %s, %s, NOW())
            """
            self.cursor.execute(sql, (
                usuario_id,
                titulo.strip(),
                descripcion.strip() if descripcion else None
            ))
            self.conexion.commit()
            return True
        except Exception as e:
            print(f"Error al crear nota: {e}")
            self.conexion.rollback()
            return False
    
    def mostrar(self, usuario_id: int) -> list:
        try:
            self.cursor.execute(
                "SELECT id, titulo, descripcion, fecha FROM notas WHERE usuario_id = %s ORDER BY fecha DESC",
                (usuario_id,)
            )
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Error al mostrar notas: {e}")
            return []
    
    def actualizar(self, nota_id: int, usuario_id: int, titulo: str, descripcion: str) -> bool:
        try:
            sql = """
                UPDATE notas 
                SET titulo = %s, descripcion = %s, fecha = NOW() 
                WHERE id = %s AND usuario_id = %s
            """
            self.cursor.execute(sql, (
                titulo.strip(),
                descripcion.strip() if descripcion else None,
                nota_id,
                usuario_id
            ))
            self.conexion.commit()
            return self.cursor.rowcount > 0
        except Exception as e:
            print(f"Error al actualizar nota: {e}")
            self.conexion.rollback()
            return False
    
    def eliminar(self, nota_id: int, usuario_id: int) -> bool:
        try:
            self.cursor.execute(
                "DELETE FROM notas WHERE id = %s AND usuario_id = %s",
                (nota_id, usuario_id)
            )
            self.conexion.commit()
            return self.cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar nota: {e}")
            self.conexion.rollback()
            return False
    
    def obtener_por_id(self, nota_id: int, usuario_id: int) -> tuple:
        try:
            self.cursor.execute(
                "SELECT id, titulo, descripcion, fecha FROM notas WHERE id = %s AND usuario_id = %s",
                (nota_id, usuario_id)
            )
            return self.cursor.fetchone()
        except Exception as e:
            print(f"Error al obtener nota: {e}")
            return None

nota = Nota()