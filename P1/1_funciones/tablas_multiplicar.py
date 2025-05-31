"""
Crear programa que calcule e imprimacualquier tabla de multiplicar
    
    restricciones:
    1.-Sin estructuras decontrol.
    2.- sin funciones.
    
"""

tabla =[
        2*1,
        2*2,
        2*3,
        2*4,
        2*5,
        2*6,
        2*7,
        2*8,
        2*9,
        2*10
        ]

print(f"TABLA DE MULTIPLICAR DEL 2 \n\t {tabla} ")



#VERSION 1
num = int(input("inserta el numero dela tabla que deseas obtener: "))

multi = num *1
print(f"{num}*1 = {multi}")
multi = num *2
print(f"{num}*2 = {multi}")
multi = num *3
print(f"{num}*3 = {multi}")
multi = num *4
print(f"{num}*4 = {multi}")
multi = num *5
print(f"{num}*5 = {multi}")
multi = num *6
print(f"{num}*6 = {multi}")
multi = num *7
print(f"{num}*7 = {multi}")
multi = num *8
print(f"{num}*8 = {multi}")
multi = num *9
print(f"{num}*9 = {multi}")
multi = num *10
print(f"{num}*10 = {multi}")


#VERSION 2

"""
Crear programa que calcule e imprimacualquier tabla de multiplicar
    
    restricciones:
    1.-con estructuras decontrol.
    2.- sin funciones.
    
"""

num = int(input("inserte el numero de la tabla que desea imprimir: "))
for i in range (1, 11):
    multi= num *i
    print(f"{num} * {i} = {multi} ")
    
#VERSION 3

"""
Crear programa que calcule e imprimacualquier tabla de multiplicar
    
    restricciones:
    1.-con estructuras decontrol.
    2.- con funciones.
    
"""
def tablaMultiplicar(num):
    for i in range (1, 11):
        print(f"{num} * {i} = {num *i} ")
    return num
    

def tabla (numero):
    num = numero
    respuesta = ""
    for i in range (1,11):
        multi = num * i
        respuesta += f"\t{num} x {i} = {multi}\n"

    return respuesta

num = int(input("Ingrese el numero de la tabla de multiplicar: "))
resultado = tabla(num)
print (f"{resultado}") 