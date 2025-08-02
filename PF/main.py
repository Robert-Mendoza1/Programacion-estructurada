# main.py
from autenticacion import login
from usuarios.usuarios import gestion_usuarios
from inventario.inventario import gestion_inventario
from proveedores.proveedores import gestion_proveedores
from ventas.ventas import gestion_ventas
from funciones import mostrar_menu_principal
from conexionBD import configurar_base_datos

def main():
    """ Función principal del programa """
    # Configurar base de datos si no existe
    configurar_base_datos()
    
    # Autenticación
    usuario_actual = login()
    if not usuario_actual:
        return
    
    # Menú principal
    while True:
        mostrar_menu_principal(usuario_actual)
        
        if usuario_actual['rol'] == 'admin':
            opciones_validas = ['1', '2', '3', '4', '5']
        else:
            opciones_validas = ['1', '2', '3', '4']
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion not in opciones_validas:
            print("\nOpción no válida. Intente nuevamente.")
            continue
            
        if opcion == '1':
            gestion_inventario()
        elif opcion == '2':
            gestion_ventas(usuario_actual)
        elif opcion == '3':
            gestion_proveedores()
        elif opcion == '4' and usuario_actual['rol'] == 'admin':
            gestion_usuarios(usuario_actual)
        elif opcion == '4' or opcion == '5':
            print("\nSesión terminada. ¡Hasta pronto!")
            break

if __name__ == '__main__':
    main()