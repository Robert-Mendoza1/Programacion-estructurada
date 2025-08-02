# ventas/ventas.py
from conexionBD import crear_conexion
from mysql.connector import Error
from datetime import datetime

def gestion_ventas(usuario_actual):
    """ Menú de gestión de ventas """
    while True:
        print("\n--- Gestión de Ventas ---")
        print("1. Nueva venta")
        print("2. Historial de ventas")
        print("3. Detalle de venta")
        print("4. Volver al menú principal")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == '1':
            nueva_venta(usuario_actual)
        elif opcion == '2':
            historial_ventas()
        elif opcion == '3':
            detalle_venta()
        elif opcion == '4':
            break
        else:
            print("\nOpción no válida. Intente nuevamente.")

def nueva_venta(usuario_actual):
    """ Procesar una nueva venta """
    print("\n--- Nueva Venta ---")
    
    conn = crear_conexion()
    if conn is None:
        return
    
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT id, nombre, precio, stock FROM productos WHERE stock > 0 ORDER BY nombre')
        productos = cursor.fetchall()
        
        if not productos:
            print("\nNo hay productos disponibles para vender")
            return
        
        print("\n--- Productos Disponibles ---")
        print("{:<5} {:<20} {:<10} {:<10}".format("ID", "Nombre", "Precio", "Stock"))
        print("-" * 45)
        
        for producto in productos:
            print("{:<5} {:<20} {:<10.2f} {:<10}".format(
                producto['id'], producto['nombre'], float(producto['precio']), producto['stock']))
        
        # Inicializar total como Decimal o float
        from decimal import Decimal
        total = Decimal('0.0')  # Cambio importante aquí
        
        items = []
        
        while True:
            producto_id = input("\nIngrese ID del producto (0 para terminar): ")
            
            if producto_id == '0':
                break
                
            try:
                cantidad = int(input("Cantidad: "))
            except ValueError:
                print("\nError: Cantidad debe ser un número entero")
                continue
                
            producto_encontrado = None
            for p in productos:
                if str(p['id']) == producto_id:
                    producto_encontrado = p
                    break
            
            if not producto_encontrado:
                print("\nError: Producto no encontrado")
                continue
                
            if cantidad <= 0:
                print("\nError: Cantidad debe ser mayor a cero")
                continue
                
            if cantidad > producto_encontrado['stock']:
                print(f"\nError: No hay suficiente stock (disponible: {producto_encontrado['stock']})")
                continue
                
            # Convertir el precio a Decimal si no lo es ya
            precio = Decimal(str(producto_encontrado['precio']))
            subtotal = precio * Decimal(cantidad)
            total += subtotal  # Ahora ambos son Decimal
            
            items.append({
                'id': producto_encontrado['id'],
                'nombre': producto_encontrado['nombre'],
                'precio': float(precio),  # Guardamos como float para consistencia
                'cantidad': cantidad,
                'subtotal': float(subtotal)
            })
            
            print(f"\nProducto agregado: {producto_encontrado['nombre']} x {cantidad} = {float(subtotal):.2f}")
            print(f"Total acumulado: {float(total):.2f}")
        
        if not items:
            print("\nVenta cancelada (no hay items)")
            return
            
        # Mostrar resumen de la venta
        print("\n--- Resumen de Venta ---")
        print("{:<5} {:<20} {:<10} {:<10} {:<10}".format(
            "ID", "Producto", "Precio", "Cantidad", "Subtotal"))
        print("-" * 55)
        
        for item in items:
            print("{:<5} {:<20} {:<10.2f} {:<10} {:<10.2f}".format(
                item['id'], item['nombre'], item['precio'], 
                item['cantidad'], item['subtotal']))
        
        print("-" * 55)
        print(f"Total a pagar: {float(total):.2f}")
        
        confirmar = input("\nConfirmar venta (S/N)? ").lower()
        
        if confirmar != 's':
            print("\nVenta cancelada")
            return
            
        # Registrar la venta (convertir total a float para MySQL)
        cursor.execute('INSERT INTO ventas (id_usuario, total) VALUES (%s, %s)', 
                      (usuario_actual['id'], float(total)))
        venta_id = cursor.lastrowid
        
        # Registrar los detalles
        for item in items:
            cursor.execute('''
                INSERT INTO detalle_ventas 
                (id_venta, id_producto, cantidad, precio_unitario, subtotal)
                VALUES (%s, %s, %s, %s, %s)
            ''', (venta_id, item['id'], item['cantidad'], item['precio'], item['subtotal']))
            
            cursor.execute('UPDATE productos SET stock = stock - %s WHERE id = %s', 
                          (item['cantidad'], item['id']))
        
        conn.commit()
        print(f"\nVenta registrada exitosamente! N° {venta_id}")
        
    except Error as e:
        print(f"\nError al procesar venta: {e}")
        conn.rollback()
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def historial_ventas():
    """ Mostrar historial de ventas """
    conn = crear_conexion()
    if conn is not None:
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute('''
                SELECT v.id, v.fecha, CONCAT(u.nombre, ' ', u.apellido) as vendedor, v.total
                FROM ventas v
                JOIN usuarios u ON v.id_usuario = u.id
                ORDER BY v.fecha DESC
                LIMIT 50
            ''')
            
            ventas = cursor.fetchall()
            
            if not ventas:
                print("\nNo hay ventas registradas")
                return
            
            print("\n--- Historial de Ventas (últimas 50) ---")
            print("{:<8} {:<20} {:<25} {:<10}".format(
                "N° Venta", "Fecha", "Vendedor", "Total"))
            print("-" * 65)
            
            for venta in ventas:
                print("{:<8} {:<20} {:<25} {:<10.2f}".format(
                    venta['id'], venta['fecha'].strftime('%Y-%m-%d %H:%M:%S'), 
                    venta['vendedor'], venta['total']))
                    
        except Error as e:
            print(f"Error al obtener historial: {e}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

def detalle_venta():
    """ Mostrar detalle de una venta específica """
    historial_ventas()
    venta_id = input("\nIngrese el N° de venta a consultar: ")
    
    conn = crear_conexion()
    if conn is not None:
        try:
            cursor = conn.cursor(dictionary=True)
            
            # Obtener información general de la venta
            cursor.execute('''
                SELECT v.id, v.fecha, CONCAT(u.nombre, ' ', u.apellido) as vendedor, v.total
                FROM ventas v
                JOIN usuarios u ON v.id_usuario = u.id
                WHERE v.id = %s
            ''', (venta_id,))
            
            venta = cursor.fetchone()
            
            if not venta:
                print("\nError: Venta no encontrada")
                return
            
            print("\n--- Detalle de Venta ---")
            print(f"N° Venta: {venta['id']}")
            print(f"Fecha: {venta['fecha'].strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"Vendedor: {venta['vendedor']}")
            print(f"Total: {venta['total']:.2f}")
            
            # Obtener items de la venta
            cursor.execute('''
                SELECT p.nombre, dv.cantidad, dv.precio_unitario, dv.subtotal
                FROM detalle_ventas dv
                JOIN productos p ON dv.id_producto = p.id
                WHERE dv.id_venta = %s
            ''', (venta_id,))
            
            items = cursor.fetchall()
            
            print("\n--- Productos Vendidos ---")
            print("{:<20} {:<10} {:<10} {:<10}".format(
                "Producto", "Cantidad", "Precio", "Subtotal"))
            print("-" * 50)
            
            for item in items:
                print("{:<20} {:<10} {:<10.2f} {:<10.2f}".format(
                    item['nombre'], item['cantidad'], item['precio_unitario'], item['subtotal']))
                    
        except Error as e:
            print(f"Error al obtener detalle: {e}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()