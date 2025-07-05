"""# proyecto-3-
# -Crear-un-proyecto que permita Gestionar (Administrar) calificaciones, colocar un-menu-de-opciones para agregar, eliminar, mmostar y calcular el promedio..
# Notas:
# 1.--Utilizar funciones y mandar llamar desde otro archivo
# 2.--Utilizar listas para almacenar los siguientes atributos: (nombre y 3 calificaciones de los alumnos).

"""

import calificaciones

def main():
    opcion = True
    datos =[]
    while opcion:
        calificaciones.borrarPantalla()
        opcion=calificaciones.menu_principal()

        match opcion:
            case "1":
                calificaciones.agregar_calificaciones(datos)
                calificaciones.esperarTecla()
            case "2":
                calificaciones.mostrar_calificaciones(datos)
                calificaciones.esperarTecla()
            case "3":
                calificaciones.calcular_promedios(datos)
                calificaciones.esperarTecla()
            case "4":
                opcion = False
                calificaciones.borrarPantalla()
                print("terminaste la ejecucuib del SW")
            case _:
                opcion = True
                input("\n\tOpción inválida, vuelva a intentarlo.... por favor")
                calificaciones.esperarTecla()

if __name__ == "__main__":
    main()