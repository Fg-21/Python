numero1 = int (input("Introduce el primer número"))

numero2 = int (input("Introduce el segundo número"))

if numero1 > numero2:
    print (numero2, numero1)
elif numero2 > numero1:
    print (numero1, numero2)
else:
    print("Son iguales")