# Crea un programa que cree una lista de enteros de tamaño 100 y lo rellene con valores enteros aleatorios entre 1 y 10. 
# Luego pedirá un valor N y mostrará cuántas veces aparece N.

#importar Random
import random

#numero de veces que se encuentra el numero
matches = 0

#lista
lista = [] 

#rellenar la lista con numeros aleatorios del 1 al 10
for iterator in range (100):
    lista.append(random.randint(1,10))

#preguntar al usuario el numero a encontrar
search = int(input("Introduce el numero para decirte cuantas veces aparece en la lista: "))

#recorrer la lista de forma manual sumando cada concordancia con el numero introducido con el usuario
for iterator in range(len(lista)):
    if search == lista[iterator]:
        matches += 1


# decir las concordancias encontradas
print("En la lista aparece el número '" + str(search) + "'" , str(matches) + " veces")