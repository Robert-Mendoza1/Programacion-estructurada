"""
  Una función es un conjunto de instrucciones agrupadas bajo un nombre en particular como un programa mas pequeño que cumple una funcion especifica. La funcion se puede reutulizar con el simple hecho de invocarla es decir mandarla llamar 

  Sintaxis:

   def nombredeMifuncion(parametros):
      bloque o conjunto de instrucciones

   nombredeMifuncion(parametros)

   Las funciones pueden ser de 4 tipos
  
    Funciones de tipo "Procedimiento" 
   1.- Funcion que no recibe parametros y no regresa valor
   3.- Funcion que recibe parametros y no regresa valor
    
    Funciones de tipo "Funcion"
   2.- Funcion que no recibe parametros y regresa valor
   4.- Funcion que recibe parametros y regresa valor

"""


#1.- Funcion que no recibe parametros y no regresa valor
def solicitarDatos1():
    nombre = input ("Nombre:")
    telefono = input("Telefono:")
    print (f"el nombre del contacto es: {nombre} y su telefonoes : {telefono}")
#3.- Funcion que recibe parametros y no regresa valor
def solicitarDatos2(nom, tel):
    nombre = nom
    telefono = tel
    print (f"el nombre del contacto es: {nom} y su telefonoes : {tel}")
    

#2.- Funcion que no recibe parametros y regresa valor
def solicitarDatos3():
    nombre = input ("Nombre:")
    telefono = input("Telefono:")
    return nombre.telefono
#4.- Funcion que recibe parametros y regresa valor
def solicitarDatos4(nom, tel):
    nombre = nom
    telefono = tel
    return nombre, telefono

#invocar las funciones
solicitarDatos1()

solicitarDatos2()
print("\n\t Agenda Telefonica \n\t\t Nombre:{nom} \n\t\tTelefono:{tel}")

nombre = input("Nombre:")
telefono =input("Telefono:")
solicitarDatos3(nombre, telefono)

nombre = input("Nombre:")
telefono =input("Telefono:")
nom, tel = solicitarDatos4(nombre, telefono)
print("\n\t Agenda Telefonica \n\t\t Nombre:{nom} \n\t\tTelefono:{tel}")