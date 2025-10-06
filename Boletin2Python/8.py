# Diseña un programa que registre las ventas de una tienda en un diccionario, 
# donde las claves son los nombres de los productos y los valores son las cantidades vendidas. 
# El programa debe permitir al usuario agregar nuevas ventas y 
# calcular el total de ventas para un producto específico. 
# Implementa un menú con ambas opciones. 

# diccionario de las ventas
dic = {}


#Agregacion de una venta. True si se ha agregado correctamente y false si no
def addSell(nombre, cantidad):
    result = False
    if nombre not in dic:
        dic[nombre] = cantidad
        result = True        
    return result

#Calcular total de ventas
def calcSells():
    return sum(dic.values())

#menu con las opciones
def menu():
    print("1. Agregar Venta")
    print("2. Calcular suma de Ventas")
    print("3. Salir")

#Imprime menu y pregunta al usuario la opcion
menu()
select = int(input("Qué quieres hacer? "))

#Bucle principal del programa
while select != 3:
    #Segun la seleccion, haremos un metodo u otro
    match select:
        #Añadir
        case 1:
            #Preguntamos nombre y cantidad de la venta
            nombre = input("Nombre de la venta: ")
            cantidad = int(input("Cantidad de la venta: "))

            #Intentar añadir al diccionario e informar del resultado
            print("Venta añadida" if addSell(nombre, cantidad) else "Venta no añadida")
        
        #Sumar todas las cantidades de las ventas
        case 2:
            #imprimir el resultado
            print("Cantidad total:", calcSells())
    
    #Imprime menu y pregunta al usuario la opcion
    menu()
    select = int(input("Qué quieres hacer? "))

print("SALIENDO...")