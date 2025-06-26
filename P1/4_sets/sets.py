"""
 Sets.- 
  Es un tipo de datos para tener una coleccion de valores pero no tiene ni indice ni orden

  Set es una colección desordenada, inmutable* y no indexada. No hay miembros duplicados.
"""
import os
os.system("clear")


paises = {"México", "Brazil", "España", "Canada", "Canada"}
print(paises)

varios =  {True,"Cadena", 23, 3.1416}
print(varios)

paises.add("Mexico")
print(paises)

varios.pop()
print(varios)

varios.remove("Cadena")
print(varios)