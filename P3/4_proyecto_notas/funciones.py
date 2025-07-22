def borrarPantalla():
  import os  
  os.system("clear")

def esperarTecla():
  input("\n\t\t ... ⚠️ Oprima cualquier tecla para continuar ⚠️ ...")

def menu_principal():
   print(".:: Sistema de Gestión de Notas ::.. \n1.-  Registro  \n2.-  Login \n3.- Salir ")
   opcion=input("Elige una opción: ").upper() 
   return opcion   