from conexionBD import *
from funciones import limpiar_pantalla, esperar_tecla, validar_numero

def menu_proveedores():
    while True:
        limpiar_pantalla()
        print("\nGESTIÓN DE PROVEEDORES")
        print("1. Agregar proveedor")
        print("2. Mostrar proveedores")
        print("3. Buscar proveedor")
        print("4. Actualizar proveedor")
        print("5. Eliminar proveedor")
        print("6. Volver al menú principal")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            agregar_proveedor()
        elif opcion == "2":
            mostrar_proveedores()
        elif opcion == "3":
            buscar_proveedor()
        elif opcion == "4":
            actualizar_proveedor()
        elif opcion == "5":
            eliminar_proveedor()
        elif opcion == "6":
            break
        else:
            print("Opción no válida")
            esperar_tecla()

def agregar_proveedor():
    limpiar_pantalla()
    print("\nAGREGAR NUEVO PROVEEDOR")
    
    # Validación de nombre (obligatorio)
    while True:
        nombre = input("Nombre del proveedor: ").strip()
        if nombre:
            break
        print("¡Error! El nombre del proveedor es obligatorio")
    
    # Validación de teléfono (formato básico)
    while True:
        telefono = input("Teléfono: ").strip()
        if telefono:  # Validación básica de teléfono
            if len(telefono) >= 8 and telefono.isdigit():
                break
            print("Error: Teléfono debe tener al menos 8 dígitos")
        else:
            print("¡Error! El teléfono es obligatorio")
    
    # Resto de campos
    contacto = input("Persona de contacto (opcional): ").strip()
    
    # Validación de email (formato básico si se proporciona)
    while True:
        email = input("Email (opcional): ").strip()
        if not email or '@' in email:  # Validación muy básica
            break
        print("Error: Formato de email inválido (debe contener @)")
    
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            sql = """INSERT INTO proveedores 
                     (nombre, contacto, telefono, email) 
                     VALUES (%s, %s, %s, %s)"""
            valores = (nombre, contacto if contacto else None, telefono, email if email else None)
            cursor.execute(sql, valores)
            conexion.commit()
            print("\n¡Proveedor agregado exitosamente!")
        except Error as e:
            print(f"Error al agregar proveedor: {e}")
        finally:
            esperar_tecla()

def mostrar_proveedores():
    limpiar_pantalla()
    print("\nLISTA DE PROVEEDORES")
    
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM proveedores")
            proveedores = cursor.fetchall()
            
            if proveedores:
                for proveedor in proveedores:
                    print(f"ID: {proveedor[0]}, Nombre: {proveedor[1]}, Contacto: {proveedor[2]}, "
                          f"Teléfono: {proveedor[3]}, Email: {proveedor[4]}")
            else:
                print("No hay proveedores registrados.")
        except Error as e:
            print(f"Error al mostrar proveedores: {e}")
        finally:
            esperar_tecla()

def buscar_proveedor():
    limpiar_pantalla()
    print("\nBUSCAR PROVEEDOR")
    
    id_proveedor = validar_numero("Ingrese el ID del proveedor: ")
    
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM proveedores WHERE id = %s", (id_proveedor,))
            proveedor = cursor.fetchone()
            
            if proveedor:
                print(f"ID: {proveedor[0]}, Nombre: {proveedor[1]}, Contacto: {proveedor[2]}, "
                      f"Teléfono: {proveedor[3]}, Email: {proveedor[4]}")
            else:
                print("Proveedor no encontrado.")
        except Error as e:
            print(f"Error al buscar proveedor: {e}")
        finally:
            esperar_tecla()
            
def actualizar_proveedor():
    limpiar_pantalla()
    print("\nACTUALIZAR PROVEEDOR")
    
    id_proveedor = validar_numero("Ingrese el ID del proveedor a actualizar: ")
    
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM proveedores WHERE id = %s", (id_proveedor,))
            proveedor = cursor.fetchone()
            
            if proveedor:
                nombre = input(f"Nuevo nombre (actual: {proveedor[1]}): ") or proveedor[1]
                contacto = input(f"Nueva persona de contacto (actual: {proveedor[2]}): ") or proveedor[2]
                telefono = input(f"Nuevo teléfono (actual: {proveedor[3]}): ") or proveedor[3]
                email = input(f"Nuevo email (actual: {proveedor[4]}): ") or proveedor[4]
                
                sql = """UPDATE proveedores 
                         SET nombre = %s, contacto = %s, telefono = %s, email = %s 
                         WHERE id = %s"""
                valores = (nombre, contacto, telefono, email, id_proveedor)
                cursor.execute(sql, valores)
                conexion.commit()
                print("\nProveedor actualizado exitosamente!")
            else:
                print("Proveedor no encontrado.")
        except Error as e:
            print(f"Error al actualizar proveedor: {e}")
        finally:
            esperar_tecla()
            
def eliminar_proveedor():
    limpiar_pantalla()
    print("\nELIMINAR PROVEEDOR")
    
    id_proveedor = validar_numero("Ingrese el ID del proveedor a eliminar: ")
    
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM proveedores WHERE id = %s", (id_proveedor,))
            proveedor = cursor.fetchone()
            
            if proveedor:
                cursor.execute("DELETE FROM proveedores WHERE id = %s", (id_proveedor,))
                conexion.commit()
                print("\nProveedor eliminado exitosamente!")
            else:
                print("Proveedor no encontrado.")
        except Error as e:
            print(f"Error al eliminar proveedor: {e}")
        finally:
            esperar_tecla()
            
