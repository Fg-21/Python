def suma (n1, n2):
    return n1 + n2
def resta (n1, n2):
    return n1 - n2
def multiplica (n1, n2):
    return n1 * n2
def divide (n1, n2):
    return n1 / n2

numero1 = int(input ("Numero 1"))
numero2 = int(input ("Numero 2"))
opcion = int(input ("Opcion (1 Suma, 2 Resta, 3 Multiplica, 4 Divide)"))

match opcion:
    case 1:
        print(suma(numero1, numero2))
    case 2:
        print(resta(numero1, numero2))
    case 3:
        print(multiplica(numero1, numero2))
    case 4:
        print(divide(numero1, numero2)) 