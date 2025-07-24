import os
import platform
import re

def borrarPantalla():
    """Limpia la pantalla de manera multiplataforma"""
    os.system("cls" if platform.system() == "Windows" else "clear")

def esperarTecla():
    """Pausa hasta que el usuario presione una tecla"""
    input("\n\t\t... ⚠️ Presione cualquier tecla para continuar ⚠️...")

def menu_usuarios():
    """Muestra el menú principal de usuarios"""
    print("\n\t.:: SISTEMA DE GESTIÓN DE NOTAS ::.")
    print("\t1. Registro de usuario")
    print("\t2. Iniciar sesión")
    print("\t3. Salir")
    return input("\tElija una opción: ").strip().upper()

def menu_notas():
    """Muestra el menú de gestión de notas"""
    print("\n\t.:: MENÚ DE NOTAS ::.")
    print("\t1. Crear nota")
    print("\t2. Mostrar notas")
    print("\t3. Modificar nota")
    print("\t4. Eliminar nota")
    print("\t5. Volver")
    return input("\tElija una opción: ").strip().upper()

def validar_email(email):
    """Valida que el formato de email sea correcto"""
    return re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email) is not None