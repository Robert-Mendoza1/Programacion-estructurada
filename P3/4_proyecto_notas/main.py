from funciones import *
from usuarios.usuario import usuario
from notas.nota import nota
import getpass

def gestion_notas(usuario_id, nombre, apellidos):
    while True:
        borrarPantalla()
        print(f"\n\t.:: BIENVENIDO {nombre} {apellidos} ::.")
        print("\t" + "="*40)
        opcion = menu_notas()

        if opcion == "1" or opcion == "CREAR":
            borrarPantalla()
            print("\n\t..:: CREAR NUEVA NOTA ::..")
            
            titulo = input("\n\tTítulo: ").strip()
            while not titulo:
                print("\t❌ El título no puede estar vacío")
                titulo = input("\tTítulo: ").strip()
                
            descripcion = input("\tDescripción (opcional): ").strip()
            
            if nota.crear(usuario_id, titulo, descripcion):
                print("\n\t✅ Nota creada exitosamente!")
            else:
                print("\n\t❌ Error al crear la nota")
            esperarTecla()

        elif opcion == "2" or opcion == "MOSTRAR":
            borrarPantalla()
            print("\n\t..:: TUS NOTAS ::..")
            
            notas = nota.mostrar(usuario_id)
            if notas:
                print("\n\t{:<5} {:<20} {:<30} {:<15}".format(
                    "ID", "Título", "Descripción", "Fecha"))
                print("\t" + "-"*80)
                for n in notas:
                    desc = n[2] if n[2] else "Sin descripción"
                    print("\t{:<5} {:<20} {:<30} {:<15}".format(
                        n[0], n[1][:18] + "..." if len(n[1]) > 18 else n[1], 
                        desc[:28] + "..." if len(desc) > 28 else desc, 
                        n[3].strftime("%d/%m/%Y")))
            else:
                print("\n\tNo tienes notas creadas aún")
            esperarTecla()

        elif opcion == "3" or opcion == "MODIFICAR":
            borrarPantalla()
            print("\n\t..:: MODIFICAR NOTA ::..")
            
            notas = nota.mostrar(usuario_id)
            if notas:
                print("\n\t{:<5} {:<20}".format("ID", "Título"))
                print("\t" + "-"*25)
                for n in notas:
                    print("\t{:<5} {:<20}".format(n[0], n[1][:18] + "..." if len(n[1]) > 18 else n[1]))
                
                try:
                    id_nota = int(input("\n\tID de la nota a modificar: "))
                    nueva_nota = nota.obtener_por_id(id_nota, usuario_id)
                    
                    if nueva_nota:
                        print(f"\n\tEditando nota: {nueva_nota[1]}")
                        nuevo_titulo = input("\tNuevo título (dejar vacío para mantener actual): ").strip()
                        nueva_desc = input("\tNueva descripción (dejar vacío para mantener actual): ").strip()
                        
                        if not nuevo_titulo:
                            nuevo_titulo = nueva_nota[1]
                        if not nueva_desc:
                            nueva_desc = nueva_nota[2]
                            
                        if nota.actualizar(id_nota, usuario_id, nuevo_titulo, nueva_desc):
                            print("\n\t✅ Nota actualizada correctamente!")
                        else:
                            print("\n\t❌ Error al actualizar la nota")
                    else:
                        print("\n\t❌ No existe una nota con ese ID")
                except ValueError:
                    print("\n\t❌ Debes ingresar un número válido")
            else:
                print("\n\tNo tienes notas para modificar")
            esperarTecla()

        elif opcion == "4" or opcion == "ELIMINAR":
            borrarPantalla()
            print("\n\t..:: ELIMINAR NOTA ::..")
            
            notas = nota.mostrar(usuario_id)
            if notas:
                print("\n\t{:<5} {:<20}".format("ID", "Título"))
                print("\t" + "-"*25)
                for n in notas:
                    print("\t{:<5} {:<20}".format(n[0], n[1][:18] + "..." if len(n[1]) > 18 else n[1]))
                
                try:
                    id_nota = int(input("\n\tID de la nota a eliminar: "))
                    confirmar = input("\t¿Estás seguro? (S/N): ").upper()
                    
                    if confirmar == "S":
                        if nota.eliminar(id_nota, usuario_id):
                            print("\n\t✅ Nota eliminada correctamente!")
                        else:
                            print("\n\t❌ Error al eliminar la nota o no existe")
                    else:
                        print("\n\tOperación cancelada")
                except ValueError:
                    print("\n\t❌ Debes ingresar un número válido")
            else:
                print("\n\tNo tienes notas para eliminar")
            esperarTecla()

        elif opcion == "5" or opcion == "SALIR":
            break

        else:
            print("\n\t❌ Opción no válida")
            esperarTecla()

def main():
    while True:
        borrarPantalla()
        opcion = menu_usuarios()

        if opcion == "1" or opcion == "REGISTRO":
            borrarPantalla()
            print("\n\t..:: REGISTRO DE USUARIO ::..\n")
            
            nombre = input("\tNombre: ").strip()
            while not nombre:
                print("\t❌ El nombre no puede estar vacío")
                nombre = input("\tNombre: ").strip()
            
            apellidos = input("\tApellidos: ").strip()
            while not apellidos:
                print("\t❌ Los apellidos no pueden estar vacíos")
                apellidos = input("\tApellidos: ").strip()
            
            email = input("\tEmail: ").lower().strip()
            while not validar_email(email):
                print("\t❌ Email no válido. Ejemplo: usuario@dominio.com")
                email = input("\tEmail: ").lower().strip()
            
            password = getpass.getpass("\tContraseña (mínimo 8 caracteres): ").strip()
            while len(password) < 8:
                print("\t❌ La contraseña debe tener al menos 8 caracteres")
                password = getpass.getpass("\tContraseña (mínimo 8 caracteres): ").strip()
            
            password_confirm = getpass.getpass("\tConfirme la contraseña: ").strip()
            while password != password_confirm:
                print("\t❌ Las contraseñas no coinciden")
                password_confirm = getpass.getpass("\tConfirme la contraseña: ").strip()
            
            if usuario.registrar(nombre, apellidos, email, password):
                print("\n\t✅ Usuario registrado correctamente!")
            else:
                print("\n\t❌ Error: El email ya está registrado o hubo un problema")
            
            esperarTecla()

        elif opcion == "2" or opcion == "LOGIN":
            borrarPantalla()
            print("\n\t..:: INICIO DE SESIÓN ::..\n")
            
            intentos = 3
            while intentos > 0:
                email = input("\tEmail: ").lower().strip()
                password = getpass.getpass("\tContraseña: ").strip()
                
                usuario_data = usuario.iniciar_sesion(email, password)
                
                if usuario_data:
                    usuario_id = usuario_data[0]
                    nombre = usuario_data[1]
                    apellidos = usuario_data[2]
                    
                    print(f"\n\t✅ Bienvenido {nombre} {apellidos}!")
                    esperarTecla()
                    gestion_notas(usuario_id, nombre, apellidos)
                    break
                else:
                    intentos -= 1
                    if intentos > 0:
                        print(f"\n\t❌ Credenciales incorrectas. Te quedan {intentos} intentos.")
                        esperarTecla()
                        borrarPantalla()
                    else:
                        print("\n\t❌ Has agotado tus intentos. Volviendo al menú principal...")
                        esperarTecla()

        elif opcion == "3" or opcion == "SALIR":
            print("\n\tSaliendo del sistema...")
            break
            
        else:
            print("\n\t❌ Opción no válida")
            esperarTecla()

if __name__ == "__main__":
    main()