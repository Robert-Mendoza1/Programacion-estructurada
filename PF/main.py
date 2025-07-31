from inventario.inventario import menu_inventario
from proveedores.proveedores import menu_proveedores
from funciones import limpiar_pantalla, esperar_tecla

def main():
    while True:
        limpiar_pantalla()
        print("\nSISTEMA DE GESTIÓN DE TIENDA")
        print("1. Gestión de Inventario")
        print("2. Gestión de Proveedores")
        print("3. Salir")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            menu_inventario()
        elif opcion == "2":
            menu_proveedores()
        elif opcion == "3":
            print("\nSaliendo del sistema...")
            break
        else:
            print("Opción no válida")
            esperar_tecla()

if __name__ == "__main__":
    main()