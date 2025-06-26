"""
Crear un proyecto que permita gerionar(Administrar) peliculas, colocar un menu de opciones para agrega, 
eliminar, modificar, consultar, buscar y baciar peliculas.

notas:
1.-Utilizar funciones y mandar llamar desde otro archivo
2.-Utiliozar una lista para almacenar los nombres de las peliculas
como se puede borrar un lista (Clear)
"""
peliculas = ["Lilo y Stich", "Concierto Juanga", "G20", "Guerra mundia Z"]

import peliculas

opcion=True
while opcion:
    peliculas.borrarPantalla()
    print("\n\t..::: CINEPOLIS CLON :::... \n..::: Sistema de Gestión de Peliculas :::...\n 1.- Agregar  \n 2.- Eliminar \n 3.- Actualizar \n 4.- Consultar \n 5.- Buscar \n 6.- Vaciar \n 7.- SALIR ")
    opcion=input("\t Elige una opción: ").upper()

    match opcion:
        case "1":
            peliculas.agregarPeliculas()
            peliculas.esperarTecla()
        case "2":
            peliculas.eliminarPeliculas()
            peliculas.esperarTecla()
            print(".:: Eliminar Peliculas ::.") 
            input("Oprima cualquier tecla para continuar ...") 
        case "3":
            peliculas.modificarPeliculas()
            peliculas.esperarTecla()
            print(".:: Modificar Peliculas ::.") 
            input("Oprima cualquier tecla para continuar ...")    
        case "4":
            peliculas.consultarPeliculas() 
            peliculas.esperarTecla()
        case "5": 
            peliculas.buscarPeliculas()
            peliculas.esperarTecla()
        case "6": 
            peliculas.vaciarPeliculas()
            peliculas.esperarTecla()
        case "7":
            opcion=False    
            peliculas.eliminarPeliculas()
            print("\n\t\t Terminaste la ejecucion del SW")
        case _: 
            opcion = True
            input("\n\t\tOpción invalida vuelva a intentarlo ... por favor")
            
            
