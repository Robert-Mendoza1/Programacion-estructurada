# conexionBD.py
import mysql.connector
from mysql.connector import Error

def crear_conexion():
    """ Crear una conexión a la base de datos MySQL """
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',  # Cambiar por tu usuario de MySQL
            password='',  # Cambiar por tu contraseña
            database='bd_proyectofinal'
        )
        return conn
    except Error as e:
        print(f"Error al conectar a MySQL: {e}")
    return None

def configurar_base_datos():
    """ Configurar la base de datos si no existe """
    try:
        # Conexión sin especificar base de datos
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password=''
        )
        
        cursor = conn.cursor()
        
        # Crear base de datos si no existe
        cursor.execute("CREATE DATABASE IF NOT EXISTS tienda")
        cursor.execute("USE tienda")
        
        # Crear tablas
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(50) UNIQUE NOT NULL,
                password VARCHAR(100) NOT NULL,
                nombre VARCHAR(50) NOT NULL,
                apellido VARCHAR(50) NOT NULL,
                rol ENUM('admin', 'empleado') NOT NULL,
                activo TINYINT(1) DEFAULT 1
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS proveedores (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(100) NOT NULL,
                contacto VARCHAR(100) NOT NULL,
                telefono VARCHAR(20) NOT NULL,
                email VARCHAR(100),
                direccion TEXT
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS productos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(100) NOT NULL,
                descripcion TEXT,
                precio DECIMAL(10,2) NOT NULL,
                stock INT NOT NULL,
                id_proveedor INT,
                FOREIGN KEY (id_proveedor) REFERENCES proveedores(id) ON DELETE SET NULL
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS ventas (
                id INT AUTO_INCREMENT PRIMARY KEY,
                fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                id_usuario INT,
                total DECIMAL(10,2) NOT NULL,
                FOREIGN KEY (id_usuario) REFERENCES usuarios(id) ON DELETE SET NULL
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS detalle_ventas (
                id INT AUTO_INCREMENT PRIMARY KEY,
                id_venta INT,
                id_producto INT,
                cantidad INT NOT NULL,
                precio_unitario DECIMAL(10,2) NOT NULL,
                subtotal DECIMAL(10,2) NOT NULL,
                FOREIGN KEY (id_venta) REFERENCES ventas(id) ON DELETE CASCADE,
                FOREIGN KEY (id_producto) REFERENCES productos(id) ON DELETE SET NULL
            )
        ''')
        
        # Insertar usuario admin si no existe
        cursor.execute("SELECT * FROM usuarios WHERE username = 'admin'")
        if not cursor.fetchone():
            cursor.execute('''
                INSERT INTO usuarios (username, password, nombre, apellido, rol)
                VALUES (%s, %s, %s, %s, %s)
            ''', ('admin', 'admin123', 'Administrador', 'Principal', 'admin'))
        
        conn.commit()
        print("Base de datos y tablas creadas exitosamente.")
        
    except Error as e:
        print(f"Error al configurar la base de datos: {e}")
        if conn.is_connected():
            conn.rollback()
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == '__main__':
    configurar_base_datos()