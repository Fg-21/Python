#Crea un programa que pida diez números reales por teclado, los almacene en una lista,
#  y luego lo recorra para averiguar el máximo y mínimo y mostrarlos por pantalla.

#lista
lista = []

#bucle para pedir 10 numeros
for cont in range(10):
    numero = int(input("Di el numero para almacenarlo en la lista: "))
    lista.append(numero)

print("Máximo:", max(lista))
print("Mínimo:", min(lista))