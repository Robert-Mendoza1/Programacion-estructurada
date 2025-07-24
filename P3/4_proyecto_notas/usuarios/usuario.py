from conexionBD import conexion_bd
import hashlib
import hmac
import secrets
from datetime import datetime

class Usuario:
    def __init__(self):
        self.conexion = conexion_bd.get_conexion()
        self.cursor = conexion_bd.get_cursor()
    
    @staticmethod
    def _hash_password(password: str, salt: str = None) -> str:
        """Genera hash seguro con salt"""
        salt = salt or secrets.token_hex(16)
        return f"{salt}${hashlib.sha256((salt + password).encode()).hexdigest()}"
    
    def registrar(self, nombre: str, apellidos: str, email: str, password: str) -> bool:
        try:
            if not all([nombre, apellidos, email, password]) or len(password) < 8:
                return False
                
            self.cursor.execute("SELECT id FROM usuarios WHERE email = %s", (email,))
            if self.cursor.fetchone():
                return False
                
            sql = """
                INSERT INTO usuarios 
                (nombre, apellidos, email, password, fecha) 
                VALUES (%s, %s, %s, %s, %s)
            """
            self.cursor.execute(sql, (
                nombre.strip().upper(),
                apellidos.strip().upper(),
                email.lower().strip(),
                self._hash_password(password),
                datetime.now()
            ))
            self.conexion.commit()
            return True
        except Exception as e:
            print(f"Error en registro: {e}")
            self.conexion.rollback()
            return False
    
    def iniciar_sesion(self, email: str, password: str) -> tuple:
        try:
            self.cursor.execute("SELECT * FROM usuarios WHERE email = %s", (email.lower().strip(),))
            usuario = self.cursor.fetchone()
            
            if usuario:
                salt, hashed = usuario[4].split('$')
                if hmac.compare_digest(self._hash_password(password, salt), usuario[4]):
                    return usuario
            return None
        except Exception as e:
            print(f"Error en login: {e}")
            return None

usuario = Usuario()