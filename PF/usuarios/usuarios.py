from conexionBD import crear_conexion
from mysql.connector import Error
from funciones import borrarPantalla, esperarTecla

def gestion_usuarios(usuario_actual):
    borrarPantalla()
    """ Menú de gestión de usuarios """
    if usuario_actual['rol'] != 'admin':
        print("\n❌ Error: No tienes permisos para acceder a esta sección")
        esperarTecla()
        return
    
    while True:
        borrarPantalla()
        print("\n👥 --- Gestión de Usuarios ---")
        print("1️⃣ 1. Listar usuarios")
        print("➕ 2. Agregar usuario")
        print("✏️ 3. Editar usuario")
        print("🚫 4. Desactivar usuario")
        print("🔙 5. Volver al menú principal")
        
        opcion = input("\n👉 Seleccione una opción: ")
        
        if opcion == '1':
            listar_usuarios()
        elif opcion == '2':
            agregar_usuario()
        elif opcion == '3':
            editar_usuario()
        elif opcion == '4':
            desactivar_usuario()
        elif opcion == '5':
            break
        else:
            print("\n❌ Opción no válida. Intente nuevamente.")
            esperarTecla()

def listar_usuarios():
    borrarPantalla()
    """ Listar todos los usuarios activos """
    conn = crear_conexion()
    if conn is not None:
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute('''
                SELECT id, username, nombre, apellido, rol 
                FROM usuarios 
                WHERE activo = 1
                ORDER BY id
            ''')
            
            usuarios = cursor.fetchall()
            
            print("\n👥 --- Lista de Usuarios ---")
            print("{:<5} {:<15} {:<20} {:<10}".format(
                "🆔 ID", "👤 Usuario", "📛 Nombre Completo", "🎭 Rol"))
            print("-" * 50)
            
            for usuario in usuarios:
                nombre_completo = f"{usuario['nombre']} {usuario['apellido']}"
                print("{:<5} {:<15} {:<20} {:<10}".format(
                    usuario['id'], usuario['username'], nombre_completo, usuario['rol']))
                    
        except Error as e:
            print(f"❌ Error al listar usuarios: {e}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
    esperarTecla()
    borrarPantalla()

def agregar_usuario():
    borrarPantalla()
    """ Agregar un nuevo usuario """
    print("\n➕ --- Agregar Nuevo Usuario ---")
    username = input("👤 Nombre de usuario: ")
    password = input("🔑 Contraseña: ")
    nombre = input("📛 Nombre: ")
    apellido = input("📛 Apellido: ")
    rol = input("🎭 Rol (admin/empleado): ").lower()
    
    if rol not in ['admin', 'empleado']:
        print("\n❌ Error: Rol debe ser 'admin' o 'empleado'")
        esperarTecla()
        return
    
    conn = crear_conexion()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO usuarios (username, password, nombre, apellido, rol)
                VALUES (%s, %s, %s, %s, %s)
            ''', (username, password, nombre, apellido, rol))
            
            conn.commit()
            print("\n✅ Usuario agregado exitosamente!")
            
        except Error as e:
            print(f"\n❌ Error al agregar usuario: {e}")
            conn.rollback()
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
    esperarTecla()
    borrarPantalla()

def editar_usuario():
    borrarPantalla()
    """ Editar un usuario existente """
    listar_usuarios()
    usuario_id = input("\n✏️ Ingrese el ID del usuario a editar: ")
    
    conn = crear_conexion()
    if conn is not None:
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute('SELECT * FROM usuarios WHERE id = %s AND activo = 1', (usuario_id,))
            usuario = cursor.fetchone()
            
            if not usuario:
                print("\n❌ Error: Usuario no encontrado o inactivo")
                esperarTecla()
                return
            
            print("\n✏️ --- Editar Usuario ---")
            print("ℹ️ Deje en blanco los campos que no desea cambiar")
            
            username = input(f"👤 Nombre de usuario [{usuario['username']}]: ") or usuario['username']
            password = input("🔑 Nueva contraseña (dejar en blanco para no cambiar): ")
            nombre = input(f"📛 Nombre [{usuario['nombre']}]: ") or usuario['nombre']
            apellido = input(f"📛 Apellido [{usuario['apellido']}]: ") or usuario['apellido']
            rol = input(f"🎭 Rol (admin/empleado) [{usuario['rol']}]: ").lower() or usuario['rol']
            
            if rol not in ['admin', 'empleado']:
                print("\n❌ Error: Rol debe ser 'admin' o 'empleado'")
                esperarTecla()
                return
            
            if password:
                cursor.execute('''
                    UPDATE usuarios 
                    SET username = %s, password = %s, nombre = %s, apellido = %s, rol = %s
                    WHERE id = %s
                ''', (username, password, nombre, apellido, rol, usuario_id))
            else:
                cursor.execute('''
                    UPDATE usuarios 
                    SET username = %s, nombre = %s, apellido = %s, rol = %s
                    WHERE id = %s
                ''', (username, nombre, apellido, rol, usuario_id))
            
            conn.commit()
            print("\n✅ Usuario actualizado exitosamente!")
            
        except Error as e:
            print(f"\n❌ Error al editar usuario: {e}")
            conn.rollback()
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
    esperarTecla()
    borrarPantalla()

def desactivar_usuario():
    borrarPantalla()
    """ Desactivar un usuario (borrado lógico) """
    listar_usuarios()
    usuario_id = input("\n🚫 Ingrese el ID del usuario a desactivar: ")
    
    conn = crear_conexion()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('UPDATE usuarios SET activo = 0 WHERE id = %s', (usuario_id,))
            
            if cursor.rowcount == 0:
                print("\n❌ Error: Usuario no encontrado o ya está inactivo")
            else:
                conn.commit()
                print("\n✅ Usuario desactivado exitosamente!")
                
        except Error as e:
            print(f"\n❌ Error al desactivar usuario: {e}")
            conn.rollback()
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
    esperarTecla()
    borrarPantalla()