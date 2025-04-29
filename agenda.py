'''
Avanzado: Clases (II)¶

Realizar una clase que administre una agenda. Se debe almacenar para cada contacto el nombre, el teléfono y el email. Además deberá mostrar un menú con las siguientes opciones:

    Añadir contacto
    Lista de contactos
    Buscar contacto
    Editar contacto
    Cerrar agenda

Agenda Personal
1. Añadir Contacto
2. Lista de contactos
3. Buscar contacto
4. Editar contacto
5. Cerrar agenda
Introduzca la opción deseada: 3
---------------------
Buscador de contactos
---------------------
Introduzca el nombre del contacto: Antonio
Datos del contacto
Nombre:  Antonio
Teléfono:  644752766
E-mail:  azm630@inlumine.ual.es
'''

class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

    def __str__(self):
        return f"Nombre: {self.nombre}\nTeléfono: {self.telefono}\nE-mail: {self.email}"


class Agenda:
    def __init__(self):
        self.contactos = {}

    def añadir_contacto(self):
        print("\n--- Añadir contacto ---")
        nombre = input("Nombre: ").strip()

        while True:
            telefono = input("Teléfono: ").strip()
            if not telefono.isdigit():
                print("El teléfono debe contener solo dígitos.")
            elif len(telefono) < 9:
                print("El teléfono debe tener al menos 9 dígitos.")
            else:
                break  # Teléfono válido, salimos del bucle

        email = input("E-mail: ").strip()
        self.contactos[nombre.lower()] = Contacto(nombre, telefono, email)
        print(f"\nContacto añadido correctamente:")
        print(self.contactos[nombre.lower()])


    def listar_contactos(self):
        print("\n--- Lista de contactos ---")
        if not self.contactos:
            print("La agenda está vacía.")
        else:
            for contacto in self.contactos.values():
                print("-" * 30)
                print(contacto)

    def buscar_contacto(self):
        print("\n--- Buscador de contactos ---")
        nombre = input("Introduzca el nombre del contacto: ").strip().lower()
        contacto = self.contactos.get(nombre)
        if contacto:
            print("\nDatos del contacto")
            print(contacto)
        else:
            print(f"No se encontró el contacto '{nombre}'.")

    def editar_contacto(self):
        print("\n--- Editar contacto ---")
        nombre = input("Nombre del contacto a editar: ").strip().lower()
        contacto = self.contactos.get(nombre)
        if contacto:
            nuevo_nombre = input(f"Nuevo nombre ({contacto.nombre}): ").strip() or contacto.nombre
            nuevo_telefono = input(f"Nuevo teléfono ({contacto.telefono}): ").strip() or contacto.telefono
            nuevo_email = input(f"Nuevo email ({contacto.email}): ").strip() or contacto.email

            # Actualizar o crear el nuevo contacto
            self.contactos[nuevo_nombre.lower()] = Contacto(nuevo_nombre, nuevo_telefono, nuevo_email)

            # Eliminar el contacto anterior si se cambió el nombre
            if nuevo_nombre.lower() != nombre:
                del self.contactos[nombre]

            print("\nContacto actualizado:")
            print(self.contactos[nuevo_nombre.lower()])  # Mostrar el contacto actualizado
        else:
            print(f"No se encontró el contacto '{nombre}'.")


    def menu(self):
        while True:
            print("\nAgenda Personal")
            print("1. Añadir Contacto")
            print("2. Lista de contactos")
            print("3. Buscar contacto")
            print("4. Editar contacto")
            print("5. Cerrar agenda")

            opcion = input("Introduzca la opción deseada: ").strip()

            if opcion == "1":
                self.añadir_contacto()
            elif opcion == "2":
                self.listar_contactos()
            elif opcion == "3":
                self.buscar_contacto()
            elif opcion == "4":
                self.editar_contacto()
            elif opcion == "5":
                print("Agenda cerrada. ¡Hasta pronto!")
                break
            else:
                print("Opción no válida. Intente de nuevo.")

# Iniciar la agenda
agenda = Agenda()
agenda.menu()