import os

def borrarPantalla():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def esperarTecla():
    input("\n\t🕒Oprima cualquier tecla para continuar...🕒\n\t")
    
def menu_principal():
    borrarPantalla()
    print("\n\t\t..::: Sistema de Gestión de Contactos :::...\n")
    print("\t\t1️⃣ - Agregar Contacto")
    print("\t\t2️⃣ - Mostrar todos los contactos")
    print("\t\t3️⃣ - Buscar contacto por nombre")
    print("\t\t4️⃣ - Modificar contacto")
    print("\t\t5️⃣ - Borrar contacto")
    print("\t\t6️⃣ - SALIR")
    return input("\n\t\t👉🏽 Elige una opción (1-6): 👈🏽").strip()

def validar_telefono(telefono):
    return len(telefono) == 10 and telefono.isdigit()

def validar_correo(correo):
    return '@' in correo and '.' in correo.split('@')[-1]



def agregar_contacto(agenda):
    borrarPantalla()
    print("\n\t\t...:: Agregar Contacto :::...\n")

    nombre = ""
    while not nombre:
        nombre = input("\n\tIngrese el nombre del contacto: ").strip().upper()
        if not nombre:
            print("\t¡El nombre no puede estar vacío!")

    # Validación del teléfono
    telefono = ""
    while not validar_telefono(telefono):
        telefono = input("\n\tIngrese el número de teléfono (10 dígitos): ").strip()
        if not validar_telefono(telefono):
            print("\t¡Debe tener exactamente 10 dígitos numéricos!")

    correo = ""
    while not validar_correo(correo):
        correo = input("\n\tIngrese el correo electrónico: ").strip().lower()
        if not validar_correo(correo):
            print("\t¡Formato de correo inválido!")

    # Agregar el contacto al diccionario
    agenda[nombre] = {
        'telefono': telefono,
        'correo': correo
    }
    
    print(f"\n\t\tContacto {nombre} agregado exitosamente.")
    return agenda


def mostrar_contactos(agenda):
    borrarPantalla()
    print("\n\t\t...:: Lista de Contactos :::...\n")
    
    if not agenda:
        print("\n\t\tNo hay contactos registrados.")
    else:
        print("\t{:<20} {:<15} {:<30}".format(
            "NOMBRE", "TELÉFONO", "EMAIL"))
        print("\t" + "-"*65)
        
        for nombre, datos in sorted(agenda.items()):
            print("\t{:<20} {:<15} {:<30}".format(
                nombre,
                datos['telefono'],
                datos['correo']))
    

def buscar_contacto(agenda):
    borrarPantalla()
    print("\n\t\t..::: Buscar Contacto :::...\n")
    nombre_buscar = input("\n\t\tIngrese el nombre del contacto a buscar: ").strip().upper()
    
    encontrado = False
    for nombre in agenda:
        if nombre_buscar in nombre:
            contacto = agenda[nombre]
            print("\n\t\tContacto encontrado:")
            print(f"\t\tNombre: {nombre}")
            print(f"\t\tTeléfono: {contacto['telefono']}")
            print(f"\t\tCorreo: {contacto['correo']}")
            encontrado = True
    
    if not encontrado:
        print(f"\n\t\tNo se encontró ningún contacto con el nombre {nombre_buscar}.")

def modificar_contactos(agenda):
    borrarPantalla()
    print("\n\t\t..::: Modificar Contacto :::...\n")
    nombre_modificar = input("\n\t\tIngrese el nombre del contacto a modificar: ").strip().upper()
    
    if nombre_modificar in agenda:
        print("\n\t\tDatos actuales:")
        print(f"\t\tNombre: {nombre_modificar}")
        print(f"\t\tTeléfono: {agenda[nombre_modificar]['telefono']}")
        print(f"\t\tCorreo: {agenda[nombre_modificar]['correo']}")
        
        # Nuevos datos
        print("\n\t\tIngrese los nuevos datos (deje en blanco para mantener el actual):")
        
        # Nuevo nombre
        nuevo_nombre = input("\n\t\tNuevo nombre: ").strip().upper()
        nuevo_nombre = nuevo_nombre if nuevo_nombre else nombre_modificar
            
        # Nuevo teléfono
        nuevo_telefono = ""
        telefono_valido = False
        while not telefono_valido:
            nuevo_telefono = input("\n\t\tNuevo teléfono (10 dígitos): ").strip()
            if not nuevo_telefono:
                nuevo_telefono = agenda[nombre_modificar]['telefono']
                telefono_valido = True
            elif validar_telefono(nuevo_telefono):
                telefono_valido = True
            else:
                print("\t¡Debe tener exactamente 10 dígitos numéricos!")
        
        # Nuevo correo
        nuevo_correo = ""
        correo_valido = False
        while not correo_valido:
            nuevo_correo = input("\n\t\tNuevo correo electrónico: ").strip().lower()
            if not nuevo_correo:
                nuevo_correo = agenda[nombre_modificar]['correo']
                correo_valido = True
            elif validar_correo(nuevo_correo):
                correo_valido = True
            else:
                print("\t¡Formato de correo inválido!")
        
        # Actualizar el contacto
        if nuevo_nombre != nombre_modificar:
            agenda[nuevo_nombre] = {
                'telefono': nuevo_telefono,
                'correo': nuevo_correo
            }
            del agenda[nombre_modificar]
        else:
            agenda[nombre_modificar] = {
                'telefono': nuevo_telefono,
                'correo': nuevo_correo
            }
            
        print(f"\n\t\tContacto modificado exitosamente.")
    else:
        print(f"\n\t\tNo se encontró ningún contacto con el nombre {nombre_modificar}.")
    

def borrar_contactos(agenda):
    borrarPantalla()
    print("\n\t\t..::: Borrar Contacto :::...\n")
    nombre_borrar = input("\n\t\tIngrese el nombre del contacto a borrar: ").strip().upper()
    
    if nombre_borrar in agenda:
        confirmacion = input(f"\n\t\t¿Está seguro de borrar a {nombre_borrar}? (S/N): ").upper()
        if confirmacion == 'S':
            del agenda[nombre_borrar]
            print(f"\n\t\tContacto {nombre_borrar} borrado exitosamente.")
        else:
            print("\n\t\tOperación cancelada.")
    else:
        print(f"\n\t\tNo se encontró ningún contacto con el nombre {nombre_borrar}.")
    
    
