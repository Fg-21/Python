numero = int(input("Introduce el numero para calcular su factorial"))

for cont in range (numero - 1, 0, -1):
    numero *= cont

print(numero)