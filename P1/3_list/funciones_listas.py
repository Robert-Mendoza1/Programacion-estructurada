'''
List (Array)
son collecciones o conjunto de datos/valores
bajo.

un mismo nombre, para accededer a los valores se hace con un 
indice numerico.

nota: sus valoressi son modificables.

La lista es una coleccion ordenada y modificable. permite miembros duplicados.
'''

import os
os.system("cls")
#Funciones mas comunes en las listas

paises =["Mexico", "Brasil", "España", "Canada"]
numero = [23,45,8,24]
varios =["hola", 3.1416,33,True]

#impirmir el contenidod e una lista 

print(paises)
print(numero)
print(varios)

#Recorrer una lista e impriir el contenido 
#1ra. forma

for i in paises:
    print(i)
    
lista = "["    
for i in paises:
    lista = lista+f"{i}"
    print(lista+"]")

#2da forma
for i in range(0,4):
    print(paises[i])
    
    
lista = "["    
for i in range(0,len(paises)):
    lista = lista+f"{i}"
    print(lista+"]")



#ordenar elementos de la s listas
os.system("cls")
print(paises)
print(numero)
print(varios)


paises.sort()
print(paises)
numero.sort()
print(numero)

#dar vuelta a las listas

varios.reverse()
print(varios)
numero.reverse()
print(numero)
paises.reverse()
print(paises)

#Buscar un elemento dentro d euna lista 

print("España" in paises)


#Insertar, añadir, agregar un elemento a una lista 
os.system("cls")

print(paises)

#1ta forma para agregar
paises.append("México")
print(paises)

#2da forma
paises.insert(1,"México")
print(paises)

#Borrar, eliminar, suprimir, quitar un elemento de la lista

os.system("cls")
print(paises)

#1ra forma
paises.pop(0)
print(paises)

#2da forma
paises.remove("México")
print(paises)


paises.sort()

#Obtener el indice opla pocision en la cual se encuentra un elemento
os.system("cls")
print(paises)

posicion=paises.index("Canada")
print(posicion)
paises.pop(posicion)
print(paises)


#contar el numero de veces que un elemento se encuentra en una lista

os.system("cls")
print(numero)

cuantas=numero.count(45)
print(cuantas)

cuantas=numero.count(23)
print(cuantas)

cuantas=numero.count(233)
print(cuantas)


#Unir el contenido de una lista en otra
os.system("cls")
print(numero)


numeros2 = [100,200]
print(numeros2)


#Crear un programa que una la slistas numero 1 y 2 e imprimia el contenido de lista resultante en forma decendente

os.system("cls")
numero.extend(numeros2)
print(numero)

numero.sort()
print(numero)
numero.reverse()
print(numero)


