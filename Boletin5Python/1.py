import os


#Clase persona con atributos de nombre, edad y altura. Contructor y getters de todos sus atributos
class Persona:
    def __init__(self, nombre, edad, altura):
        self.__nombre = nombre
        self.__edad = edad
        self.__altura = altura

    def getNombre(self):
        return self.__nombre
    
    def getEdad(self):
        return self.__edad
    
    def getAltura(self):
        return self.__altura
    
    def __str__(self):
        return f"{self.__nombre}, {self.__edad}, {self.__altura}"

#Devuelve una lista de personas con los atributos leidos en el txt
def readPersonas(ruta):
    listaPersonas = []
    with open(ruta, "r") as f:
       for linea in f:
           nombre, edad, altura = linea.strip().split(",")
           edad = int(edad)
           altura = float(altura)
           listaPersonas.append(Persona(nombre, altura, edad))
    return listaPersonas

#calcula la media de edades y alturas y las devuelve en una lista donde el primer indice es la media de alturas y el segundo la media de edades
def calculaMedia(listaPersons):
    sumAges = 0
    sumHeights = 0
    for persona in listaPersons:
        if isinstance(persona, Persona):
            sumAges += persona.getEdad()
            sumHeights += persona.getAltura()
    media = [sumAges/len(listaPersons), 
             sumHeights/len(listaPersons)]
    return media    



#estructura principal ejecutable
if __name__ == "__main__":
    #Creacion de la lista de personas
    lista = [Persona("Juan", "22", "1.76"),
            Persona("Pedro", "26", "1.46"),
            Persona("Mar", "32", "1.81")]

    #Obtener la carpeta desde donde se ejecuta el archivo de python y juntarla con el nombre para hacer la ruta
    carpeta = os.path.dirname(__file__)
    ruta_archivo = os.path.join(carpeta, "alumnos.txt")

    #Creacion y escritura del archivo
    with open(ruta_archivo, "w") as f:
        for person in lista:
            f.write(person.__str__() + "\n")

    #recoleccion de datos del fichero
    personas = readPersonas(ruta_archivo)

    #obtencion de la media de edades y alturas a partir de la lista de personas
    medias = calculaMedia(personas)

    #imprimir los nombres de las personas
    print("NOMBRES:")
    for persona in personas:
        if isinstance(persona, Persona):
            print(persona.getNombre())
    
    #imprimir medias de edad y altura
    print(f"Media de alturas: {medias[0]}, Media de edad: {medias[1]}")
        
    




    
