from conexionBD import *
from funciones import limpiar_pantalla, esperar_tecla, validar_numero, validar_entero

def menu_inventario():
    while True:
        limpiar_pantalla()
        print("\nGESTIÓN DE INVENTARIO")
        print("1. Agregar producto")
        print("2. Mostrar productos")
        print("3. Buscar producto")
        print("4. Actualizar producto")
        print("5. Eliminar producto")
        print("6. Volver al menú principal")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            mostrar_productos()
        elif opcion == "3":
            buscar_producto()
        elif opcion == "4":
            actualizar_producto()
        elif opcion == "5":
            eliminar_producto()
        elif opcion == "6":
            break
        else:
            print("Opción no válida")
            esperar_tecla()

def agregar_producto():
    limpiar_pantalla()
    print("\nAGREGAR NUEVO PRODUCTO")
    
    # Validación de nombre (no puede estar vacío)
    while True:
        nombre = input("Nombre del producto: ").strip()
        if nombre:  # Si no está vacío
            break
        print("¡Error! El nombre del producto es obligatorio")
    
    # Resto de validaciones
    precio = validar_numero("Precio: ")
    stock = validar_entero("Stock inicial: ")
    categoria = input("Categoría (opcional): ")
    
    # Validación de proveedor (puede ser opcional)
    while True:
        try:
            proveedor_id = input("ID del proveedor (dejar vacío si no aplica): ").strip()
            if not proveedor_id:  # Si está vacío
                proveedor_id = None
                break
            proveedor_id = int(proveedor_id)
            if proveedor_id > 0:
                break
            print("Error: ID debe ser mayor a 0")
        except ValueError:
            print("Error: Debe ingresar un número entero válido")
    
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            sql = """INSERT INTO productos 
                     (nombre, precio, stock, categoria, proveedor_id) 
                     VALUES (%s, %s, %s, %s, %s)"""
            valores = (nombre, precio, stock, categoria if categoria else None, proveedor_id)
            cursor.execute(sql, valores)
            conexion.commit()
            print("\n¡Producto agregado exitosamente!")
        except Error as e:
            print(f"Error al agregar producto: {e}")
        finally:
            esperar_tecla()

# ... (resto de funciones de inventario)
def mostrar_productos():
    limpiar_pantalla()
    print("\nLISTA DE PRODUCTOS")
    
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM productos")
            productos = cursor.fetchall()
            
            if productos:
                for producto in productos:
                    print(f"ID: {producto[0]}, Nombre: {producto[1]}, Precio: {producto[2]}, "
                          f"Stock: {producto[3]}, Categoría: {producto[4]}, Proveedor ID: {producto[5]}")
            else:
                print("No hay productos registrados.")
        except Error as e:
            print(f"Error al mostrar productos: {e}")
        finally:
            esperar_tecla()
            
def buscar_producto():
    limpiar_pantalla()
    print("\nBUSCAR PRODUCTO")
    
    nombre = input("Ingrese el nombre del producto a buscar: ")
    
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM productos WHERE nombre LIKE %s", (f"%{nombre}%",))
            productos = cursor.fetchall()
            
            if productos:
                for producto in productos:
                    print(f"ID: {producto[0]}, Nombre: {producto[1]}, Precio: {producto[2]}, "
                          f"Stock: {producto[3]}, Categoría: {producto[4]}, Proveedor ID: {producto[5]}")
            else:
                print("No se encontraron productos con ese nombre.")
        except Error as e:
            print(f"Error al buscar producto: {e}")
        finally:
            esperar_tecla()
            
def actualizar_producto():
    limpiar_pantalla()
    print("\nACTUALIZAR PRODUCTO")
    
    producto_id = validar_entero("Ingrese el ID del producto a actualizar: ")
    
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM productos WHERE id = %s", (producto_id,))
            producto = cursor.fetchone()
            
            if producto:
                nombre = input(f"Nuevo nombre (actual: {producto[1]}): ") or producto[1]
                precio = validar_numero(f"Nuevo precio (actual: {producto[2]}): ") or producto[2]
                stock = validar_entero(f"Nuevo stock (actual: {producto[3]}): ") or producto[3]
                categoria = input(f"Nueva categoría (actual: {producto[4]}): ") or producto[4]
                proveedor_id = validar_entero(f"Nuevo ID de proveedor (actual: {producto[5]}): ") or producto[5]
                
                sql = """UPDATE productos 
                         SET nombre = %s, precio = %s, stock = %s, 
                             categoria = %s, proveedor_id = %s 
                         WHERE id = %s"""
                valores = (nombre, precio, stock, categoria if categoria else None, 
                           proveedor_id if proveedor_id > 0 else None, producto_id)
                cursor.execute(sql, valores)
                conexion.commit()
                
                print("\nProducto actualizado exitosamente!")
            else:
                print("Producto no encontrado.")
        except Error as e:
            print(f"Error al actualizar producto: {e}")
        finally:
            esperar_tecla()
            
def eliminar_producto():
    limpiar_pantalla()
    print("\nELIMINAR PRODUCTO")
    
    producto_id = validar_entero("Ingrese el ID del producto a eliminar: ")
    
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM productos WHERE id = %s", (producto_id,))
            producto = cursor.fetchone()
            
            if producto:
                cursor.execute("DELETE FROM productos WHERE id = %s", (producto_id,))
                conexion.commit()
                print("\nProducto eliminado exitosamente!")
            else:
                print("Producto no encontrado.")
        except Error as e:
            print(f"Error al eliminar producto: {e}")
        finally:
            esperar_tecla()