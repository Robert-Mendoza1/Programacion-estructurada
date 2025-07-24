import os
import agenda

def main():
    opcion = True
    while opcion:
        os.system("cls" if os.name == "nt" else "clear")
        print("\n\t\t.:: AGENDA DE CONTACTOS ::.")
        print("\n1. Agregar contacto")
        print("2. Mostrar contactos")
        print("3. Buscar contacto")
        print("4. Modificar contacto")
        print("5. Eliminar contacto")
        print("6. Salir")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            agenda.agregar_contacto()
        elif opcion == "2":
            agenda.mostrar_contactos()
        elif opcion == "3":
            agenda.buscar_contacto()
        elif opcion == "4":
            agenda.modificar_contacto()
        elif opcion == "5":
            agenda.borrar_contacto()
        elif opcion == "6":
            opcion = False
            os.system("cls" if os.name == "nt" else "clear")
            print("Terminaste la ejecución del software.")
        else:
            input("\n\tOpción inválida, vuelva a intentarlo...")
                  
if __name__ == "__main__":
    main()