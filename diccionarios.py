'''
Escribir un programa que permita gestionar la base de datos de clientes de una empresa. Los 
clientes se guardarán en un diccionario en el que la clave de cada cliente será su NIF, y el
valor será otro diccionario con los datos del cliente (nombre, dirección, teléfono, correo). 
El programa debe preguntar al 
usuario por una opción del siguiente menú: (1) Añadir cliente, (2) Eliminar cliente, 
(3) Mostrar cliente, (4) Listar todos los clientes, 
(6) Terminar. En función de la opción 
elegida el programa tendrá que hacer lo siguiente:

Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
Preguntar por el NIF del cliente y mostrar sus datos.
Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
Terminar el programa.

'''
clientes={}

opcion=''
while opcion!='6':
    if opcion=='1':
        nif=input("Por favor, ingresa tu NIF: ")
        nombre= input("Por favor, ingresa tu nombre: ")
        direccion= input("Por favor, ingresa tu dirección: ")
        telefono= input("Por favor, ingresa tu telefono: ")
        email= input("Por favor, ingresa tu email: ")
        cliente= {'nombre':nombre, 'direccion': direccion , 'telefono':telefono , "correo": email}
        clientes[nif]= cliente
    if opcion=="2":
        nif= input("Ingresa el NIF del cliente: ")
        if nif in clientes:
            del clientes[nif]
        else:
            print("NIF no encontrado")
        
    if opcion=='3':
        nif= input("Ingresa el NIF del cliente: ")
        if nif in clientes:
            for clave,valor in clientes[nif].items():
                print(clave,'  :  ', valor)
        else:
            print("NIF no encontrado")
    if opcion=='4':
        for clave, valor in clientes.items():
            print(clave,'  :  ', valor["nombre"])
    
        
    opcion= input("1. Agregar un usuario \n 2. Eliminar un usuario \n 3. Mostrar un usuario \n4. Mostrar todo\n6. Salir \n Elige una opción: ")
        
    


