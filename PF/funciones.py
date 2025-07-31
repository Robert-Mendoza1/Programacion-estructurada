import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def esperar_tecla():
    input("\nPresione cualquier tecla para continuar...")

def validar_numero(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            return valor
        except ValueError:
            print("Error: Debe ingresar un número válido")

def validar_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("Error: Debe ingresar un número entero válido")