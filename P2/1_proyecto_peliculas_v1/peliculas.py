
peliculas = []


def borrarPantalla():
    import os
    os.system("cls")
    
def esperarTecla():
    input("seleccion una opcion: ")
    
def agregarPeliculas():
    borrarPantalla()
    print("\n\t\tAgregar pelicula")
    peliculas.append(input("\nIngrese el nombre").upper().strip())
    
    print("\n\t\tLA OPERACION SE REALIZO CON EXITO")
    
    
def consultarPeliculas ():
    borrarPantalla()
    print("\n\t\tConsultar peliculas")
    
    if len(peliculas)>0:
        for i in range (0,len(peliculas)):
            print(f"{i+1} : {peliculas[i]}")
    else:
        print("\n\t\tNo hay peliculas en el sistema")
        
def vaciarPeliculas():
    borrarPantalla()
    print("\n\t\tLimpiar/borrar todas las peliculas")
    resp = input("¿Deseas borrar las peliculas?(Si/No)").lower
    
    if resp == "si":
        peliculas.clear()
        print("\n\t\t la operacion se realizo con exito")
        
        
        
def buscarPeliculas():
    borrarPantalla()
    print("\n\t\tBuscar una las peliculas")
    pelicula_buscar = input("ingresa el nombre de la pelicula a buscar: ").upper().strip()
    if not(pelicula_buscar in peliculas):
        print("\n\t No hay nunguna pelicula con este nombre")
    else:
        encontro = 0 
        for i in range(0,len(peliculas)):
            if pelicula_buscar == peliculas[i]:
                print(f"\n\t La pelicula{pelicula_buscar}si latenemos y esta casillero: {i+1} ")
                encontro += 1
        print(f"\n\tTenemos {encontro} peliculas(s) con este titulo")
        
        
def modificarPeliculas():
    borrarPantalla()
    print("\n\t\tModificar una las peliculas")
    pelicula_buscar = input("ingresa el nombre de la pelicula a buscar: ").upper().strip()
    if not(pelicula_buscar in peliculas):
        print("\n\t No hay nunguna pelicula con este nombre")
    else:
        encontro = 0 
        for i in range(0,len(peliculas)):
            if pelicula_buscar == peliculas[i]:
                resp = input("¿Deseas actualizar la pelicula? (Si/No)").lower().strip()
                if resp== "si":
                    peliculas[i]=input("\n\tIntrodusca/tecle el nuevo valos de la pelicula").upper().strip()
                    
                    print(f"\n\t La pelicula{peliculas[i]}si latenemos en el casillero: {i+1} ")
                    encontro += 1
        print(f"\n\tSe ctualizaron {encontro} peliculas(s) con este Titulo")

def eliminarPeliculas():
    borrarPantalla()
    print("\n\t\tBorrar peliculas")
    pelicula_buscar = input("ingresa el nombre de la pelicula a buscar: ").upper().strip()
    if not(pelicula_buscar in peliculas):
        print("\n\t No hay nunguna pelicula con este nombre")
    else:
        encontro = 0
        for i in range(0,len(peliculas)):
            if pelicula_buscar == peliculas[i]:
                resp = input("¿Deseas eliminar la pelicula? (Si/No)").lower().strip()
                if resp== "si":
                    del peliculas[i]
                    print(f"\n\t La pelicula {pelicula_buscar} se elimino con exito")
                    encontro += 1
        if encontro == 0:
            print("\n\t No se elimino ninguna pelicula.")