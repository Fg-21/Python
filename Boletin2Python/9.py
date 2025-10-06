# Crea un diccionario donde las claves son las letras del abecedario y los valores, 
# la puntuación para cada letra, como en el Scrabble. El programa le pedirá una palabra al usuario 
# y se mostrará por pantalla la puntuación que tiene la palabra en total.

#diccionario
dic = {'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1,
    'J': 8, 'K': 8, 'L': 1, 'M': 3, 'N': 1, 'Ñ': 8, 'O': 1, 'P': 3, 'Q': 5,
    'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 8, 'X': 8, 'Y': 4, 'Z': 10}

# suma de la puntuacion
suma = 0

# Peticion de la palabra
word = input("Pon una palabra para calcular la puntuación: ")

# Split de la palabra por sus letras
letters = word.upper()

#recorrer la lista e ir sumando la puntuacion de cada letra
for letter in letters:
    if letter in dic:
        suma += dic[letter]

# imprimir el resultado
print (suma)