numero = int(input("Introduce un numero para ver si es primo"))
divisores = 0
for cont in range (1, numero + 1):
    if numero % cont == 0:
        divisores += 1

if divisores == 2:
    print("Es primo")
else:
    print("No es primo")