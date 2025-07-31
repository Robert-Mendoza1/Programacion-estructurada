import mysql.connector
from mysql.connector import Error

def conectar():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="bd_proyectofinal"
        )
        
        # Crear tablas si no existen
        crear_tablas(conexion)
        
        return conexion
    except Error as e:
        print(f"Error de conexión: {e}")
        return None

def crear_tablas(conexion):
    cursor = conexion.cursor()
    
    # Tabla de productos
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(100) NOT NULL,
            precio DECIMAL(10,2) NOT NULL,
            stock INT NOT NULL,
            categoria VARCHAR(50),
            proveedor_id INT
        )
    """)
    
    # Tabla de proveedores
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS proveedores (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(100) NOT NULL,
            contacto VARCHAR(100),
            telefono VARCHAR(15),
            email VARCHAR(100)
        )
    """)
    
    conexion.commit()