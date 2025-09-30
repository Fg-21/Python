import random
# Crea una lista de enteros de longitud 10 que se inicializará con números aleatorios comprendidos entre 1 y 100. 

#lista
lista = []



#bucle para rellenar la lista
for cont in range (10):
    #numero randomizado
    numero = random.randint(1,100)
    lista.append(numero)

print(lista)

