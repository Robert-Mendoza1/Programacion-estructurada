import os
import agenda

def main():
 opcion = True
 agenda_contactos = {}
 while opcion:
        os.system("cls" if os.name == "nt" else "clear")
        opcion = agenda.menu_principal()
        
        
        
        if opcion == "1":
            agenda.agregar_contacto(agenda_contactos)
            agenda.esperarTecla()
        elif opcion == "2":
            agenda.mostrar_contactos(agenda_contactos)
            agenda.esperarTecla()
        elif opcion == "3":
            agenda.buscar_contacto(agenda_contactos)
            agenda.esperarTecla()
        elif opcion == "4":
            agenda.modificar_contactos(agenda_contactos)
            agenda.esperarTecla()
        elif opcion == "5":
            agenda.borrar_contactos(agenda_contactos)
            agenda.esperarTecla()
        elif opcion == "6":
            opcion = False
            os.system("cls" if os.name == "nt" else "clear")
            print("Terminaste la ejecución del software.")
            
            
        else:
            input("\n\tOpción inválida, vuelva a intentarlo.... por favor")
            agenda.esperarTecla()
                  
if __name__ == "__main__":
    main()
    
   