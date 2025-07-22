import funciones
import conexionBD

def main():
    opcion=True
    while opcion:
        funciones.borrarPantalla()
        opcion=funciones.menu_principal()

        if opcion=="1" or opcion=="REGISTRO":
            print("Estoy en la opcion 1")
        elif opcion=="2" or opcion=="LOGIN": 
            print("Estoy en la opcion 2")  
        elif opcion=="3" or opcion=="SALIR": 
            print("Estoy en la opcion 3") 
            print("Termino la Ejecución del Sistema")
            opcion=False
            funciones.esperarTecla()  
        else:
            print("Opcion no valida")
            opcion=True
            funciones.esperarTecla() 


if __name__ == "__main__":
    main()    


