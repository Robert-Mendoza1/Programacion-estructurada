import mysql.connector
import re
from mysql.connector import Error

def borrarPantalla():
    import os  
    os.system("cls" if os.name == "nt" else "clear")

def esperarTecla():
    input("\n\t... Presiona cualquier tecla para continuar ...") 

def conectar():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="bd_agenda"
        )
        
        # Verificar y crear tabla si no existe
        cursor = conexion.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS contactos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(50) NOT NULL,
                numero VARCHAR(50) NOT NULL,
                correo VARCHAR(50) NOT NULL
            )
        """)
        conexion.commit()
        
        return conexion
    except Error as e:
        print(f"Error de conexión: {e}")
        return None

def validar_telefono(numero):
    return re.match(r'^\d{10}$', numero) is not None

def validar_correo(correo):
    return re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', correo) is not None

def agregar_contacto():
    borrarPantalla()
    conexionBD = conectar()
    if conexionBD:
        print("\n\t\t.:: AGREGAR CONTACTO ::.\n")
        
        while True:
            nombre = input("Nombre: ").strip()
            if nombre:
                break
            print("Error: El nombre no puede estar vacío")
        
        while True:
            numero = input("Teléfono (10 dígitos): ").strip()
            if validar_telefono(numero):
                break
            print("Error: Teléfono debe tener 10 dígitos numéricos")
        
        while True:
            correo = input("Correo electrónico: ").strip()
            if validar_correo(correo):
                break
            print("Error: Formato de correo inválido (ejemplo: usuario@dominio.com)")
        
        try:
            cursor = conexionBD.cursor()
            sql = """INSERT INTO contactos 
                    (nombre, numero, correo) 
                    VALUES (%s, %s, %s)"""
            val = (nombre, numero, correo)
            cursor.execute(sql, val)
            conexionBD.commit()
            print("\n\t¡CONTACTO AGREGADO CON ÉXITO!")
        except Error as e:
            print(f"Error al agregar contacto: {e}")
        finally:
            esperarTecla()

def mostrar_contactos():
    borrarPantalla()
    conexionBD = conectar()
    if conexionBD:
        try:
            cursor = conexionBD.cursor()
            sql = "SELECT id, nombre, numero, correo FROM contactos ORDER BY nombre"
            cursor.execute(sql)
            registros = cursor.fetchall()
            
            if registros:
                print("\n\t\t.:: LISTA DE CONTACTOS ::.\n")
                print(f"{'ID':<5}{'NOMBRE':<25}{'TELÉFONO':<15}{'CORREO':<25}")
                print("-"*70)
                for reg in registros:
                    print(f"{reg[0]:<5}{reg[1]:<25}{reg[2]:<15}{reg[3]:<25}")
                print("-"*70)
            else:
                print("\nNo hay contactos registrados")
        except Error as e:
            print(f"Error al mostrar contactos: {e}")
        finally:
            esperarTecla()

def buscar_contacto():
    borrarPantalla()
    conexionBD = conectar()
    if conexionBD:
        nombre = input("Ingrese nombre a buscar: ").strip()
        
        try:
            cursor = conexionBD.cursor()
            sql = "SELECT id, nombre, numero, correo FROM contactos WHERE nombre LIKE %s"
            val = (f"%{nombre}%",)
            cursor.execute(sql, val)
            registros = cursor.fetchall()
            
            if registros:
                print("\n\t\t.:: RESULTADOS DE BÚSQUEDA ::.\n")
                print(f"{'ID':<5}{'NOMBRE':<25}{'TELÉFONO':<15}{'CORREO':<25}")
                print("-"*70)
                for reg in registros:
                    print(f"{reg[0]:<5}{reg[1]:<25}{reg[2]:<15}{reg[3]:<25}")
                print("-"*70)
            else:
                print(f"\nNo se encontraron contactos con: '{nombre}'")
        except Error as e:
            print(f"Error al buscar contactos: {e}")
        finally:
            esperarTecla()

def modificar_contacto():
    borrarPantalla()
    conexionBD = conectar()
    if conexionBD:
        id_contacto = input("Ingrese ID del contacto a modificar: ").strip()
        
        try:
            cursor = conexionBD.cursor()
            sql = "SELECT * FROM contactos WHERE id = %s"
            val = (id_contacto,)
            cursor.execute(sql, val)
            contacto = cursor.fetchone()
            
            if contacto:
                print("\nDatos actuales del contacto:")
                print(f"ID: {contacto[0]}")
                print(f"Nombre: {contacto[1]}")
                print(f"Teléfono: {contacto[2]}")
                print(f"Correo: {contacto[3]}")
                print("\nIngrese nuevos datos (deje en blanco para mantener el valor actual):")
                
                nuevo_nombre = input(f"Nuevo nombre [{contacto[1]}]: ").strip()
                nuevo_nombre = nuevo_nombre if nuevo_nombre else contacto[1]
                
                while True:
                    nuevo_numero = input(f"Nuevo teléfono [{contacto[2]}]: ").strip()
                    if not nuevo_numero:
                        nuevo_numero = contacto[2]
                        break
                    if validar_telefono(nuevo_numero):
                        break
                    print("Error: Teléfono debe tener 10 dígitos numéricos")
                
                while True:
                    nuevo_correo = input(f"Nuevo correo [{contacto[3]}]: ").strip()
                    if not nuevo_correo:
                        nuevo_correo = contacto[3]
                        break
                    if validar_correo(nuevo_correo):
                        break
                    print("Error: Formato de correo inválido")
                
                confirmacion = input("\n¿Confirmar cambios? (S/N): ").upper()
                if confirmacion == "S":
                    sql = """UPDATE contactos 
                            SET nombre = %s, numero = %s, correo = %s 
                            WHERE id = %s"""
                    val = (nuevo_nombre, nuevo_numero, nuevo_correo, id_contacto)
                    cursor.execute(sql, val)
                    conexionBD.commit()
                    print("\n\t¡CONTACTO MODIFICADO CON ÉXITO!")
            else:
                print(f"\nNo se encontró contacto con ID: {id_contacto}")
        except Error as e:
            print(f"Error al modificar contacto: {e}")
        finally:
            esperarTecla()

def borrar_contacto():
    borrarPantalla()
    conexionBD = conectar()
    if conexionBD:
        id_contacto = input("Ingrese ID del contacto a eliminar: ").strip()
        
        try:
            cursor = conexionBD.cursor()
            sql = "SELECT * FROM contactos WHERE id = %s"
            val = (id_contacto,)
            cursor.execute(sql, val)
            contacto = cursor.fetchone()
            
            if contacto:
                print("\nDatos del contacto a eliminar:")
                print(f"ID: {contacto[0]}")
                print(f"Nombre: {contacto[1]}")
                print(f"Teléfono: {contacto[2]}")
                print(f"Correo: {contacto[3]}")
                
                confirmacion = input("\n¿Está seguro de eliminar este contacto? (S/N): ").upper()
                if confirmacion == "S":
                    sql = "DELETE FROM contactos WHERE id = %s"
                    val = (id_contacto,)
                    cursor.execute(sql, val)
                    conexionBD.commit()
                    print("\n\t¡CONTACTO ELIMINADO CON ÉXITO!")
            else:
                print(f"\nNo se encontró contacto con ID: {id_contacto}")
        except Error as e:
            print(f"Error al eliminar contacto: {e}")
        finally:
            esperarTecla()