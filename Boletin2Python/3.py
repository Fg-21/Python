# Realiza un programa que pida 8 números enteros y los almacene en una lista. 
# A continuación, recorrerá esa tabla y mostrará esos números junto con la palabra “par” o “impar” según proceda.

#lista
lista = []

#pedimos los 8 numeros enteros y los almacenamos
for cont in range(8):
    number = int(input("Introduce un numero: "))
    lista.append(number)

#recorremos la lista e imprimimos si son pares o no
for aux in lista:
    if (aux % 2 == 0):
        print (str(aux) + " Par")
    else:
        print (str(aux) + " Impar")