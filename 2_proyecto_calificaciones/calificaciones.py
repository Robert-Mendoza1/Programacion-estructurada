import mysql.connector
from mysql.connector import Error


'''lista=[
    ["Ruben", 10.0,8.9,9.2],
    ["Andres", 10.0,10.0,10.0],
    ["maria", 10.0,10.0,10.0]
]'''
calificaciones = []

def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla():
    input("\n\tOprima cualquier tecla para continuar...\n\t")
    
def conectar():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="bd_calificaciones"
        )
        return conexion
    except Error as e:
        print(f"El error que se presentó es: {e}")
        return None      
    
def menu_principal():
    print("\n\t\t..::: Sistema de Gestión de calificaciones.:::...\n\n\t\t-1.--Agregar--\n\t\t-2.--Mostrar--\n\t\t-3.--Buscar calificacion --\n\t\t-4.--Modificar calificacion --\n\t\t-5.--Borrar Alumno -- \n\t\t-6.--SALIR--")
    opcion = input("\n\t\t Elige una opción (1-6): ").upper()
    return opcion
                
def agregar_calificaciones(Lista):
    borrarPantalla()
    conexionBD = conectar()
    if conexionBD is not None:
        print("\n\t\t.:: Crear Calificación ::.\n")
        
        while True:
            nombre = input("\nIngresa el nombre del alumno: ").upper().strip()
            if nombre:  # Validar que no esté vacío
                break
            print("¡Error! El nombre no puede estar vacío.")
        
        while True:
            try:
                calif1 = float(input("\nIngresa la calificación 1 (0-10): "))
                if 0 <= calif1 <= 10:
                    break
                print("¡Error! La calificación debe estar entre 0 y 10.")
            except ValueError:
                print("¡Error! Debes ingresar un número válido.")
        
        while True:
            try:
                calif2 = float(input("\nIngresa la calificación 2 (0-10): "))
                if 0 <= calif2 <= 10:
                    break
                print("¡Error! La calificación debe estar entre 0 y 10.")
            except ValueError:
                print("¡Error! Debes ingresar un número válido.")
        
        while True:
            try:
                calif3 = float(input("\nIngresa la calificación 3 (0-10): "))
                if 0 <= calif3 <= 10:
                    break
                print("¡Error! La calificación debe estar entre 0 y 10.")
            except ValueError:
                print("¡Error! Debes ingresar un número válido.")
        
        promedio = round((calif1 + calif2 + calif3) / 3, 2)
        
        cursor = conexionBD.cursor()
        sql = """INSERT INTO calificaciones 
                (nombre, calificacion1, calificacion2, calificacion3, promedio) 
                VALUES (%s, %s, %s, %s, %s)"""
        val = (nombre, calif1, calif2, calif3, promedio)
        cursor.execute(sql, val)
        conexionBD.commit()
        print("\n\t::: ¡CALIFICACIÓN REGISTRADA CON ÉXITO! :::")
        esperarTecla()
    
def mostrar_calificaciones(Lista):
    borrarPantalla()
    conexionBD = conectar()
    if conexionBD is not None:
        cursor = conexionBD.cursor()
        sql = "SELECT * FROM calificaciones ORDER BY nombre"
        cursor.execute(sql)
        registros = cursor.fetchall()
        
        if registros:
            print("\n\t.:: LISTADO DE CALIFICACIONES ::.\n")
            print(f"{'ID':<5}{'NOMBRE':<20}{'CALIF1':<10}{'CALIF2':<10}{'CALIF3':<10}{'PROMEDIO':<10}")
            print("-"*65)
            for registro in registros:
                print(f"{registro[0]:<5}{registro[1]:<20}{registro[2]:<10}{registro[3]:<10}{registro[4]:<10}{registro[5]:<10}")
            print("-"*65)
        else:
            print("\n\tNo hay calificaciones registradas")

def buscar_calificacion(Lista):
    borrarPantalla()
    conexionBD = conectar()
    if conexionBD is not None:
        nombre = input("Ingresa el nombre del alumno a buscar: ").upper().strip()
        cursor = conexionBD.cursor()
        sql = "SELECT * FROM calificaciones WHERE nombre = %s"
        val = (nombre,)
        cursor.execute(sql, val)
        registros = cursor.fetchall()
        
        if registros:
            print("\n\t.:: RESULTADOS DE BÚSQUEDA ::.\n")
            print(f"{'ID':<5}{'NOMBRE':<20}{'CALIF1':<10}{'CALIF2':<10}{'CALIF3':<10}{'PROMEDIO':<10}")
            print("-"*65)
            for registro in registros:
                print(f"{registro[0]:<5}{registro[1]:<20}{registro[2]:<10}{registro[3]:<10}{registro[4]:<10}{registro[5]:<10}")
            print("-"*65)
        else:
            print(f"\n\tNo se encontraron calificaciones para {nombre}")

def modificar_calificacion(Lista):
    borrarPantalla()
    conexionBD = conectar()
    if conexionBD is not None:
        nombre = input("Ingresa el nombre del alumno a modificar: ").upper().strip()
        cursor = conexionBD.cursor()
        sql = "SELECT * FROM calificaciones WHERE nombre = %s"
        val = (nombre,)
        cursor.execute(sql, val)
        registros = cursor.fetchall()
        
        if registros:
            print("\n\t.:: DATOS ACTUALES ::.\n")
            print(f"{'ID':<5}{'NOMBRE':<20}{'CALIF1':<10}{'CALIF2':<10}{'CALIF3':<10}{'PROMEDIO':<10}")
            print("-"*65)
            for registro in registros:
                print(f"{registro[0]:<5}{registro[1]:<20}{registro[2]:<10}{registro[3]:<10}{registro[4]:<10}{registro[5]:<10}")
            print("-"*65)
            
            confirmacion = input("\n¿Deseas modificar estas calificaciones? (S/N): ").upper()
            if confirmacion == "S":
                nuevo_nombre = input("Nuevo nombre [Enter para mantener]: ").upper().strip()
                calif1 = input("Nueva calificación 1 [Enter para mantener]: ")
                calif2 = input("Nueva calificación 2 [Enter para mantener]: ")
                calif3 = input("Nueva calificación 3 [Enter para mantener]: ")
                
                # Mantener valores anteriores si no se ingresan nuevos
                if not nuevo_nombre:
                    nuevo_nombre = registros[0][1]
                if not calif1:
                    calif1 = registros[0][2]
                else:
                    calif1 = float(calif1)
                if not calif2:
                    calif2 = registros[0][3]
                else:
                    calif2 = float(calif2)
                if not calif3:
                    calif3 = registros[0][4]
                else:
                    calif3 = float(calif3)
                
                nuevo_promedio = round((calif1 + calif2 + calif3) / 3, 2)
                
                sql = """UPDATE calificaciones 
                        SET nombre = %s, calificacion1 = %s, calificacion2 = %s, 
                        calificacion3 = %s, promedio = %s 
                        WHERE id = %s"""
                val = (nuevo_nombre, calif1, calif2, calif3, nuevo_promedio, registros[0][0])
                cursor.execute(sql, val)
                conexionBD.commit()
                print("\n\t¡CALIFICACIONES ACTUALIZADAS CON ÉXITO!")
        else:
            print(f"\n\tNo se encontraron calificaciones para {nombre}")
  
def borrar_alumno(Lista):
    borrarPantalla()
    conexionBD = conectar()
    if conexionBD is not None:
        nombre = input("Ingresa el nombre del alumno a eliminar: ").upper().strip()
        cursor = conexionBD.cursor()
        sql = "SELECT * FROM calificaciones WHERE nombre = %s"
        val = (nombre,)
        cursor.execute(sql, val)
        registros = cursor.fetchall()
        
        if registros:
            print("\n\t.:: REGISTRO A ELIMINAR ::.\n")
            print(f"{'ID':<5}{'NOMBRE':<20}{'CALIF1':<10}{'CALIF2':<10}{'CALIF3':<10}{'PROMEDIO':<10}")
            print("-"*65)
            for registro in registros:
                print(f"{registro[0]:<5}{registro[1]:<20}{registro[2]:<10}{registro[3]:<10}{registro[4]:<10}{registro[5]:<10}")
            print("-"*65)
            
            confirmacion = input("\n¿Estás seguro de eliminar este registro? (S/N): ").upper()
            if confirmacion == "S":
                sql = "DELETE FROM calificaciones WHERE id = %s"
                val = (registros[0][0],)
                cursor.execute(sql, val)
                conexionBD.commit()
                print("\n\t¡REGISTRO ELIMINADO CON ÉXITO!")
        else:
            print(f"\n\tNo se encontraron calificaciones para {nombre}")

def calcular_promerios(Lista):
    borrarPantalla()
    print("\n\t\t\t..::: Calculat promedios :::...\n")
    if len(Lista) == 0:
        print(f"{'Nombre':<15}{'promedio':<10}")
        print("-"*30)
        promedio_general = 0
        for fila in Lista:
            nombre = fila[0]
            promedio = ((fila[1])+(fila[2])+(fila[3]))/3
            print(f"{fila[0]:<15}{promedio:2f}")
            promedio_clase += promedio
            print(f"El promedio del grupo es: {(promedio_clase/len(Lista)):.2f}")
            
            print("-"*30)
            print(f"son {len(Lista)} alumnos")
        else:
            print("\n\t\tNo hay calificaciones en el sistemas.")