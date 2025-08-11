from conexionBD import crear_conexion
from mysql.connector import Error
from funciones import borrarPantalla, esperarTecla

def gestion_inventario():
    borrarPantalla()
    """ Menú de gestión de inventario """
    while True:
        print("\n📋 --- Gestión de Inventario ---")
        print("1️⃣ 1. Listar productos")
        print("🔍 2. Buscar producto")
        print("➕ 3. Agregar producto")
        print("✏️ 4. Editar producto")
        print("📊 5. Ajustar stock")
        print("🔙 6. Volver al menú principal")
        
        opcion = input("\n👉 Seleccione una opción: ")
        
        if opcion == '1':
            listar_productos()
        elif opcion == '2':
            buscar_producto()
        elif opcion == '3':
            agregar_producto()
        elif opcion == '4':
            editar_producto()
        elif opcion == '5':
            ajustar_stock()
        elif opcion == '6':
            break
        else:
            print("\n❌ Opción no válida. Intente nuevamente.")
            esperarTecla()

def listar_productos():
    borrarPantalla()
    """ Listar todos los productos """
    conn = crear_conexion()
    if conn is not None:
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute('''
                SELECT p.id, p.nombre, p.descripcion, p.precio, p.stock, pr.nombre as proveedor
                FROM productos p
                LEFT JOIN proveedores pr ON p.id_proveedor = pr.id
                ORDER BY p.id
            ''')
            
            productos = cursor.fetchall()
            
            print("\n📋 --- Lista de Productos ---")
            print("{:<5} {:<20} {:<30} {:<10} {:<10} {:<20}".format(
                "🆔 ID", "📛 Nombre", "📝 Descripción", "💰 Precio", "📦 Stock", "🏢 Proveedor"))
            print("-" * 95)
            
            for producto in productos:
                print("{:<5} {:<20} {:<30} {:<10.2f} {:<10} {:<20}".format(
                    producto['id'], producto['nombre'], producto['descripcion'] or '', 
                    producto['precio'], producto['stock'], producto['proveedor'] or 'N/A'))
                    
        except Error as e:
            print(f"❌ Error al listar productos: {e}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
    esperarTecla()

def buscar_producto():
    borrarPantalla()
    """ Buscar productos por nombre o descripción """
    termino = input("\n🔍 Ingrese término de búsqueda: ")
    
    conn = crear_conexion()
    if conn is not None:
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute('''
                SELECT p.id, p.nombre, p.descripcion, p.precio, p.stock, pr.nombre as proveedor
                FROM productos p
                LEFT JOIN proveedores pr ON p.id_proveedor = pr.id
                WHERE p.nombre LIKE %s OR p.descripcion LIKE %s
                ORDER BY p.id
            ''', (f'%{termino}%', f'%{termino}%'))
            
            productos = cursor.fetchall()
            
            if not productos:
                print("\n🔎 No se encontraron productos con ese término")
                esperarTecla()
                return
            
            print("\n📋 --- Resultados de Búsqueda ---")
            print("{:<5} {:<20} {:<30} {:<10} {:<10} {:<20}".format(
                "🆔 ID", "📛 Nombre", "📝 Descripción", "💰 Precio", "📦 Stock", "🏢 Proveedor"))
            print("-" * 95)
            
            for producto in productos:
                print("{:<5} {:<20} {:<30} {:<10.2f} {:<10} {:<20}".format(
                    producto['id'], producto['nombre'], producto['descripcion'] or '', 
                    producto['precio'], producto['stock'], producto['proveedor'] or 'N/A'))
                    
        except Error as e:
            print(f"❌ Error al buscar productos: {e}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
    esperarTecla()

def agregar_producto():
    borrarPantalla()
    """ Agregar un nuevo producto al inventario """
    print("\n➕ --- Agregar Nuevo Producto ---")
    nombre = input("📛 Nombre: ")
    descripcion = input("📝 Descripción (opcional): ") or None
    precio = float(input("💰 Precio: "))
    stock = int(input("📦 Stock inicial: "))
    id_proveedor = input("🏢 ID de proveedor (opcional, dejar en blanco si no aplica): ") or None
    
    conn = crear_conexion()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO productos (nombre, descripcion, precio, stock, id_proveedor)
                VALUES (%s, %s, %s, %s, %s)
            ''', (nombre, descripcion, precio, stock, id_proveedor))
            
            conn.commit()
            print("\n✅ Producto agregado exitosamente!")
            
        except Error as e:
            print(f"\n❌ Error al agregar producto: {e}")
            conn.rollback()
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
    esperarTecla()

def editar_producto():
    borrarPantalla()
    """ Editar un producto existente """
    listar_productos()
    producto_id = input("\n✏️ Ingrese el ID del producto a editar: ")
    
    conn = crear_conexion()
    if conn is not None:
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute('SELECT * FROM productos WHERE id = %s', (producto_id,))
            producto = cursor.fetchone()
            
            if not producto:
                print("\n❌ Error: Producto no encontrado")
                esperarTecla()
                return
            
            print("\n✏️ --- Editar Producto ---")
            print("ℹ️ Deje en blanco los campos que no desea cambiar")
            
            nombre = input(f"📛 Nombre [{producto['nombre']}]: ") or producto['nombre']
            descripcion = input(f"📝 Descripción [{producto['descripcion'] or ''}]: ") or producto['descripcion']
            precio = input(f"💰 Precio [{producto['precio']}]: ") or producto['precio']
            id_proveedor = input(f"🏢 ID de proveedor [{producto['id_proveedor'] or ''}]: ") or producto['id_proveedor']
            
            cursor.execute('''
                UPDATE productos 
                SET nombre = %s, descripcion = %s, precio = %s, id_proveedor = %s
                WHERE id = %s
            ''', (nombre, descripcion, float(precio), id_proveedor, producto_id))
            
            conn.commit()
            print("\n✅ Producto actualizado exitosamente!")
            
        except Error as e:
            print(f"\n❌ Error al editar producto: {e}")
            conn.rollback()
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
    esperarTecla()

def ajustar_stock():
    borrarPantalla()
    """ Ajustar el stock de un producto """
    listar_productos()
    producto_id = input("\n📊 Ingrese el ID del producto a ajustar: ")
    cantidad = int(input("🔢 Ingrese la cantidad a agregar (use negativo para restar): "))
    
    conn = crear_conexion()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('UPDATE productos SET stock = stock + %s WHERE id = %s', (cantidad, producto_id))
            
            if cursor.rowcount == 0:
                print("\n❌ Error: Producto no encontrado")
            else:
                conn.commit()
                print("\n✅ Stock actualizado exitosamente!")
                
        except Error as e:
            print(f"\n❌ Error al ajustar stock: {e}")
            conn.rollback()
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
    esperarTecla()