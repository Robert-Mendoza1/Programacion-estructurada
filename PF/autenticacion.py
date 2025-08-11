# autenticacion.py
from conexionBD import crear_conexion
from mysql.connector import Error
import getpass

def login():
    """ Función para autenticar usuarios """
    conn = crear_conexion()
    if conn is not None:
        try:
            print("\n--- Inicio de Sesión ---")
            username = input("Usuario: ")
            password = getpass.getpass("Contraseña: ")
            
            cursor = conn.cursor(dictionary=True)
            cursor.execute('''
                SELECT id, username, nombre, apellido, rol 
                FROM usuarios 
                WHERE username = %s AND password = %s AND activo = 1
            ''', (username, password))
            
            usuario = cursor.fetchone()
            
            if usuario:
                print(f"\nBienvenido, {usuario['nombre']} {usuario['apellido']} ({usuario['rol']})")
                return usuario
            else:
                print("\nError: Usuario o contraseña incorrectos")
                return None
                
        except Error as e:
            print(f"Error al autenticar: {e}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
    return None