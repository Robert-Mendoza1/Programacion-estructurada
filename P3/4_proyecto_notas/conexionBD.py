import mysql.connector
from mysql.connector import errorcode
import configparser
import sys

class ConexionBD:
    _instancia = None
    
    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(ConexionBD, cls).__new__(cls)
            cls._instancia.inicializar_conexion()
        return cls._instancia
    
    def inicializar_conexion(self):
        try:
            config = configparser.ConfigParser()
            config.read('config.ini')
            
            db_config = {
                'host': config.get('DATABASE', 'host', fallback='localhost'),
                'user': config.get('DATABASE', 'user', fallback='root'),
                'password': config.get('DATABASE', 'password', fallback=''),
                'database': config.get('DATABASE', 'database', fallback='bd_notas'),
                'port': config.getint('DATABASE', 'port', fallback=3306)
            }
            
            self.conexion = mysql.connector.connect(**db_config)
            self.cursor = self.conexion.cursor(buffered=True)
            
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Error: Usuario o contraseña incorrectos")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Error: La base de datos no existe")
            else:
                print(f"Error de conexión: {err}")
            sys.exit(1)
        except Exception as e:
            print(f"Error inesperado: {e}")
            sys.exit(1)
    
    def get_conexion(self):
        if not self.conexion.is_connected():
            self.reconectar()
        return self.conexion
    
    def get_cursor(self):
        if not self.conexion.is_connected():
            self.reconectar()
        return self.cursor
    
    def reconectar(self):
        try:
            self.conexion.reconnect(attempts=3, delay=5)
        except mysql.connector.Error as err:
            print(f"Error al reconectar: {err}")
            sys.exit(1)
    
    def cerrar(self):
        try:
            if self.cursor:
                self.cursor.close()
            if self.conexion.is_connected():
                self.conexion.close()
        except mysql.connector.Error as err:
            print(f"Error al cerrar conexión: {err}")

conexion_bd = ConexionBD()