# Crea un diccionario donde las claves sean el conjunto 1 de la siguiente tabla y los valores, 
# el conjunto 2:

conjunto1 = ('e', 'i', 'k', 'm', 'p', 'q', 'r', 's', 't', 'u', 'v')
conjunto2 = ('p', 'v', 'i', 'u', 'm', 't', 'e', 'r', 'k', 'q', 's')

# Match de cada letra del conjunto 1 con cada letra del conjunto 2
dic = dict(zip(conjunto1, conjunto2))

#frase encriptada
frasefinal = ""

# El programa debe pedir una frase al usuario y debe mostrar la frase encriptada. Para ello, 
# cada vez que encuentre en la frase una letra del conjunto 1 la sustituirá por su correspondiente 
# en el conjunto 2.

#pregunta
word = input("Escribe la frase o palbra a encriptar: ").lower()

#recorre letra a letra de la palabra y añade a la frase encriptada el valor del conjunto 2
for letter in word:
    if letter in dic:
        frasefinal += dic[letter]
    else:
        frasefinal += letter

#imprime la palabra encriptada
print(frasefinal)
        

