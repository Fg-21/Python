
def repasa(n1, n2):
    if (n1 > n2):
        for cont in range (n2, n1 + 1):
            print (cont)
    elif (n2 > n1):
        for cont in range (n1, n2 + 1):
            print (cont)
    else:
        print("Son iguales")

numero1 = int(input("Primer número"))
numero2 = int(input("Segundo número"))
repasa(numero1, numero2)





