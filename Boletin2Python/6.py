#Escribe un programa que tome una cadena de texto como entrada y 
#genere un diccionario que cuente la frecuencia de cada palabra en el texto.

#definir el diccionario
diccionario = {}

#obtener la cadena del usuario
cadena = str(input("Introduce una cadena para contar las palabras: "))

#ponemos la cadena separada en palabras en la lista auxiliar
lista = cadena.split()

#recorrer la lista añadiendo al diccionario cada palabra, si ya está en él, se suma uno al valor
for palabra in lista:
    if palabra not in diccionario:
        diccionario[palabra] = 1
    else:
        diccionario[palabra] += 1

#imprimir el diccionario para ver las veces que aparece cada palabra
print(diccionario)
