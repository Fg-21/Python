#Crea un programa que permita al usuario agregar, eliminar y buscar contactos en una libreta de direcciones implementada como un diccionario. 
#La clave del diccionario será el nombre del contacto y el valor, su número de teléfono. 
#Crea un menú para las distintas opciones e implementa una función para cada opción.

#definicion del diccionario de contactos
contactos = {}


# Metodo de agregacion de contacto, si lo agrega correctamente (No estaba agregado antes) devuelve True, sino, devolverá False
def add(nombre, tlf):
    
    result = False
    if nombre not in contactos:
        contactos[nombre] = tlf
        result = True        
    return result

# Metodo para la eliminacion de contactos, si lo elimina correctamente (El contacto estaba agregado correctamente) devuelve True, sino, devolverá False
def delete(nombre):
    result = False
    if nombre in contactos:
        del contactos[nombre]
        result = True
    return result

# Metodo para buscar un contacto, si lo encuentra devuelve su numero y si no, "No existe el contacto" 
def search(nombre):
    return contactos.get(nombre)

# Metodo para imprimir un menu
def menu():
    print("Elige una opción:")    
    print("1. Añadir")    
    print("2. Eliminar")    
    print("3. Buscar")    
    print("4. Salir")

#Imprime menu y pregunta al usuario la opcion
menu()
select = int(input("Qué quieres hacer? "))

#Bucle principal del programa
while select != 4:
    #Segun la seleccion, haremos un metodo u otro
    match select:
        #Añadir
        case 1:
            # Preguntamos nombre y tlf del contacto a añadir
            nombre = input("Introduce el nombre del contacto: ")
            tlf = int(input("Introduce el teléfono del contacto:"))

            # Intentar añadir el contacto e informar del resultado
            print("Contacto añadido" if add(nombre, tlf) else "El contacto ya existe")
        #Eliminar
        case 2:
            # Preguntamos nombre del contacto a eliminar
            nombre = input("Nombre del contacto a eliminar: ")

            # Intentar eliminar el contacto e informar del resultado
            print("Contacto eliminado" if delete(nombre) else "No se ha encontrado el contacto a eliminar")
        
        #Buscar
        case 3:
            # Preguntamos el nombre del contacto a buscar
            nombre = input("Nombre del contacto a buscar")

            #Intentar buscar el contacto e informar del resultado
            searchresult = search(nombre)
            print("El numero asociado al contacto es: " + str(searchresult) if searchresult is not None else "Contacto no encontrado")
    
    #Imprime menu y pregunta al usuario la opcion
    menu()
    select = int(input("Qué quieres hacer? "))


print("Saliendo...") 
