# funciones.py
def mostrar_menu_principal(usuario_actual):
    """ Mostrar menú principal según el rol del usuario """
    print("\n--- Menú Principal ---")
    print(f"Usuario: {usuario_actual['nombre']} {usuario_actual['apellido']} ({usuario_actual['rol']})")
    print("\n1. Gestión de Inventario")
    print("2. Gestión de Ventas")
    print("3. Gestión de Proveedores")
    
    if usuario_actual['rol'] == 'admin':
        print("4. Gestión de Usuarios")
        print("5. Salir")
    else:
        print("4. Salir")
        
def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla():
    """Pausa hasta que el usuario presione una tecla"""
    input("\n\t\t... ⚠️ Presione cualquier tecla para continuar ⚠️...")