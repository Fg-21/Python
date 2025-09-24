numero = int(input("Introduce el numero para la base y la altura de la pirámide"))

for cont in range (0, numero + 1):
    print(" " * (numero - cont) + "* " * cont)