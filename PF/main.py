# main.py
from autenticacion import login
from usuarios.usuarios import gestion_usuarios
from inventario.inventario import gestion_inventario
from proveedores.proveedores import gestion_proveedores
from ventas.ventas import gestion_ventas
from funciones import mostrar_menu_principal
from conexionBD import configurar_base_datos
from funciones import borrarPantalla
import os
import time

def main():
    borrarPantalla()
    """ Función principal del programa """
    # Configurar base de datos si no existe
    print("⚙️ Configurando base de datos...")
    configurar_base_datos()
    
    # Autenticación
    print("\n🔐 Sistema de Autenticación")
    usuario_actual = login()
    if not usuario_actual:
        print("❌ Autenticación fallida. Saliendo del sistema...")
        time.sleep(2)
        return
    
    # Menú principal
    while True:
        borrarPantalla()
        print(f"👤 Usuario: {usuario_actual['nombre']} | Rol: {usuario_actual['rol'].capitalize()}")
        mostrar_menu_principal(usuario_actual)
        
        if usuario_actual['rol'] == 'admin':
            opciones_validas = ['1', '2', '3', '4', '5']
        else:
            opciones_validas = ['1', '2', '3', '4']
        
        opcion = input("\n👉 Seleccione una opción: ")
        
        if opcion not in opciones_validas:
            print("\n❌ Opción no válida. Intente nuevamente.")
            time.sleep(1)
            continue
        
        borrarPantalla()
        if opcion == '1':
            print("📦 Módulo de Inventario")
            print("-----------------------")
            gestion_inventario()
        elif opcion == '2':
            print("💰 Módulo de Ventas")
            print("-------------------")
            gestion_ventas(usuario_actual)
        elif opcion == '3':
            print("🚚 Módulo de Proveedores")
            print("-----------------------")
            gestion_proveedores()
        elif opcion == '4' and usuario_actual['rol'] == 'admin':
            print("👥 Módulo de Gestión de Usuarios")
            print("-------------------------------")
            gestion_usuarios(usuario_actual)
        elif opcion == '5' or (opcion == '4' and usuario_actual['rol'] != 'admin'):
            print("\n👋 Sesión terminada. ¡Hasta pronto!")
            time.sleep(2)
            break

if __name__ == '__main__':
    print("🚀 Iniciando sistema de gestión...")
    time.sleep(1)
    main()