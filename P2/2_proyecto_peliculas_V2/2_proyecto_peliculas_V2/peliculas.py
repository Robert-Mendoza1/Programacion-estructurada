"""dict u objeto para almacenar los atributos (nombre, categoria, clasificacion, genero, idioma)
pelicula = {
    "nombre": "",
    "categoria": "",
    "clasificacion": "",
    "genero": "",
    "idioma": ""
}
"""

pelicula = {}

def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla():
    input("\n\tOprima cualquier tecla para continuar...\n\t")
    
def crearPeliculas():
    borrarPantalla()
    print("\n\t.:: Alta de Películas ::.\n")
    pelicula.update({"nombre": input("Ingresa el nombre: ").upper().strip()})
    #pelicula["nombre"] = input("\n\t Ingresa el nombre: ").upper().strip()
    pelicula.update({"categoria": input("Ingresa la categoría: ").upper().strip()})
    pelicula.update({"clasificacion": input("Ingresa la clasificación: ").upper().strip()})
    pelicula.update({"genero": input("Ingresa el género: ").upper().strip()})
    pelicula.update({"idioma": input("Ingresa el idioma: ").upper().strip()})
    input("\n\t\t::: ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! :::")

def mostrarPeliculas():
    borrarPantalla()
    print("\n\t.:: Consultar o Mostrar la Película ::.\n")
    if len(pelicula) > 0:
        for i in pelicula:
            print(f"\t{i}: {pelicula[i]}")
    else:
        print("\t..:: No hay películas en el sistema ::..\n")

def borrarPeliculas():
    borrarPantalla()
    print("\n\t.:: Borrar o Quitar TODAS las Películas ::.\n")
    resp = input("¿Deseas quitar o borrar las películas? (Si/No): ").lower().strip()
    if resp == "si":
        pelicula.clear()
        input("\n\t\t::: ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! :::")

def agregarCaracteristicaPeliculas():
    borrarPantalla()
    print("\n\t.:: Agregar Característica a Películas ::.\n")
    atributo = input("Ingresa la nueva característica de la película: ").lower().strip()
    valor = input("Ingresa el valor de la característica de la película: ").upper().strip()
    pelicula.update({atributo:valor})
    pelicula[atributo] = valor
    print("\n\t\t::: ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! :::")
    
def modificarCaracteristicaPeliculas():
    borrarPantalla()
    print("\n\t.:: Modificar Característica de Películas ::.\n")
    if len(pelicula) > 0:
        for i in pelicula:
            print(f"\t{i}: {pelicula[i]}")
            resp = input(f"\n¿Deseas modificar las carecteristicas {i}? (Si/No): ").lower().strip()
        if resp == "si":
            pelicula[i] = input(f"Ingresa el nuevo valor para {i}: ").upper().strip()
            print("\n\t\t::: ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! :::") 
    else:
        print("\t..:: No hay películas en el sistema ::..\n")   


def borrarCaracteristicaPeliculas():
    borrarPantalla()
    print("\n\t.:: Borrar Característica de Películas ::.")
    if len(pelicula) > 0:
        for i in pelicula:
            print(f"\t(i): {pelicula[i]}")
        atributo = input("\n\tIngresa el nombre de la característica que deseas borrar: ").lower().strip()
        if atributo in pelicula:
            del pelicula [atributo]
            print("\n\t\t::: ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! :::")
        else:
            print("\n \t::: La característica no existe :::")
    else:
        print("\t..:: No hay películas en el sistema ::..\n")  
















"""def agregarPeliculas():
    borrarPantalla()
    print("\n\t\t.::Agregar Películas::.\n\t")
    peliculas.append(input("\nIngresa el nombre: ").upper().strip())
    print("\n\t:::¡LA OPERACIÓN SE REALIZÓ CON ÉXITO!\n\t")"""
"""def consultarPeliculas():
    borrarPantalla()
    print("\n\t\t.::Consultar o Mostrar TODAS las Películas::.\n\t")
    if len(peliculas) > 0:
        for i in range(0, len(peliculas)):
            print(f"\n\t{i+1}: {peliculas[i]}")
    else:
        print("\n\t.::No hay películas en el sistema::.\n\t")
"""
"""def vaciarPeliculas():
    borrarPantalla()
    print("\n\t\t.::Limpiar o Borrar TODAS las Películas::.\n\t")
    resp = input("¿Deseas borrar todas las películas? (Si/No)\n\t").lower()
    if resp == "si":
        peliculas.clear()
        print("\n\t:::¡LA OPERACIÓN SE REALIZÓ CON ÉXITO!:::\n\t")"""
"""ef borrarPelicula():
    borrarPantalla()
    print("\n\t\t.::Borrar Una Película::.\n\t")
    peliculabuscar = input("\n\t\t.::Dame el nombre de la película a borrar::.\n\t").upper().strip()
    if peliculabuscar in peliculas:
        resp = input("\n\t\t.::Se encontró la película::.\n\t\t.::¿Está seguro de borrar el registro de la película? (Si/No)::.\n\t").upper().strip()
        if resp == "SI":
            peliculas.remove(peliculabuscar)
            print(f"\n\tLa película se borró con éxito")
    else:
        print("\n\t.::No se encontró alguna película con este nombre, lo siento::.\n\t")"""