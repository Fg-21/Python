#Escribe un programa que lea 10 números por teclado y que luego los muestre ordenados de mayor a menor.

#lista
lista = []

#leer numeros por teclado y guardarlos en la lista
for cont in range (10):
    num = int(input("Introduce numero: "))
    lista.append(num)

#ordenar la lista
lista.sort

#mostrar lista ordenada
print(lista)
