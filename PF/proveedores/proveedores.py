# proveedores/proveedores.py
from conexionBD import crear_conexion
from mysql.connector import Error
from funciones import borrarPantalla
from funciones import esperarTecla


def gestion_proveedores():
    borrarPantalla()
    """ Menú de gestión de proveedores """
    while True:
        print("\n🏢 --- Gestión de Proveedores ---")
        print("1️⃣ 1. Listar proveedores")
        print("🔍 2. Buscar proveedor")
        print("➕ 3. Agregar proveedor")
        print("✏️ 4. Editar proveedor")
        print("🔙 5. Volver al menú principal")
        
        opcion = input("\n👉 Seleccione una opción: ")
        
        if opcion == '1':
            listar_proveedores()
        elif opcion == '2':
            buscar_proveedor()
        elif opcion == '3':
            agregar_proveedor()
        elif opcion == '4':
            editar_proveedor()
        elif opcion == '5':
            break
        else:
            print("\n❌ Opción no válida. Intente nuevamente.")

def listar_proveedores():
    borrarPantalla()
    """ Listar todos los proveedores """
    conn = crear_conexion()
    if conn is not None:
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute('SELECT id, nombre, contacto, telefono, email FROM proveedores ORDER BY id')
            
            proveedores = cursor.fetchall()
            
            print("\n🏢 --- Lista de Proveedores ---")
            print("{:<5} {:<20} {:<20} {:<15} {:<20}".format(
                "🆔 ID", "🏛️ Nombre", "👤 Contacto", "📞 Teléfono", "📧 Email"))
            print("-" * 80)
            
            for proveedor in proveedores:
                print("{:<5} {:<20} {:<20} {:<15} {:<20}".format(
                    proveedor['id'], proveedor['nombre'], proveedor['contacto'], 
                    proveedor['telefono'], proveedor['email'] or ''))
            esperarTecla()
            borrarPantalla()
                    
        except Error as e:
            print(f"❌ Error al listar proveedores: {e}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

def buscar_proveedor():
    borrarPantalla()
    """ Buscar proveedores por nombre o contacto """
    termino = input("\n🔍 Ingrese término de búsqueda: ")
    
    conn = crear_conexion()
    if conn is not None:
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute('''
                SELECT id, nombre, contacto, telefono, email
                FROM proveedores
                WHERE nombre LIKE %s OR contacto LIKE %s OR email LIKE %s
                ORDER BY id
            ''', (f'%{termino}%', f'%{termino}%', f'%{termino}%'))
            
            proveedores = cursor.fetchall()
            
            if not proveedores:
                print("\n🔎 No se encontraron proveedores con ese término")
                return
            
            print("\n🏢 --- Resultados de Búsqueda ---")
            print("{:<5} {:<20} {:<20} {:<15} {:<20}".format(
                "🆔 ID", "🏛️ Nombre", "👤 Contacto", "📞 Teléfono", "📧 Email"))
            print("-" * 80)
            
            for proveedor in proveedores:
                print("{:<5} {:<20} {:<20} {:<15} {:<20}".format(
                    proveedor['id'], proveedor['nombre'], proveedor['contacto'], 
                    proveedor['telefono'], proveedor['email'] or ''))
            esperarTecla()
            borrarPantalla()
                    
        except Error as e:
            print(f"❌ Error al buscar proveedores: {e}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

def agregar_proveedor():
    borrarPantalla()
    """ Agregar un nuevo proveedor """
    print("\n➕ --- Agregar Nuevo Proveedor ---")
    nombre = input("🏛️ Nombre: ")
    contacto = input("👤 Persona de contacto: ")
    telefono = input("📞 Teléfono: ")
    email = input("📧 Email (opcional): ") or None
    direccion = input("📍 Dirección (opcional): ") or None
    
    conn = crear_conexion()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO proveedores (nombre, contacto, telefono, email, direccion)
                VALUES (%s, %s, %s, %s, %s)
            ''', (nombre, contacto, telefono, email, direccion))
            
            conn.commit()
            print("\n✅ Proveedor agregado exitosamente!")
            esperarTecla()
            borrarPantalla()
            
        except Error as e:
            print(f"\n❌ Error al agregar proveedor: {e}")
            conn.rollback()
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

def editar_proveedor():
    borrarPantalla()
    """ Editar un proveedor existente """
    listar_proveedores()
    proveedor_id = input("\n✏️ Ingrese el ID del proveedor a editar: ")
    
    conn = crear_conexion()
    if conn is not None:
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute('SELECT * FROM proveedores WHERE id = %s', (proveedor_id,))
            proveedor = cursor.fetchone()
            
            if not proveedor:
                print("\n❌ Error: Proveedor no encontrado")
                return
            
            print("\n✏️ --- Editar Proveedor ---")
            print("ℹ️ Deje en blanco los campos que no desea cambiar")
            
            nombre = input(f"🏛️ Nombre [{proveedor['nombre']}]: ") or proveedor['nombre']
            contacto = input(f"👤 Contacto [{proveedor['contacto']}]: ") or proveedor['contacto']
            telefono = input(f"📞 Teléfono [{proveedor['telefono']}]: ") or proveedor['telefono']
            email = input(f"📧 Email [{proveedor['email'] or ''}]: ") or proveedor['email']
            direccion = input(f"📍 Dirección [{proveedor['direccion'] or ''}]: ") or proveedor['direccion']
            
            cursor.execute('''
                UPDATE proveedores 
                SET nombre = %s, contacto = %s, telefono = %s, email = %s, direccion = %s
                WHERE id = %s
            ''', (nombre, contacto, telefono, email, direccion, proveedor_id))
            
            conn.commit()
            print("\n✅ Proveedor actualizado exitosamente!")
            esperarTecla()
            borrarPantalla()
            
        except Error as e:
            print(f"\n❌ Error al editar proveedor: {e}")
            conn.rollback()
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()