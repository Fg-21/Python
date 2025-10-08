class Animal:

    def __init__(self, nombre, patas):
        self.__nombre = nombre
        self.__patas = patas
    
    def habla(self):
        return ""
    
    def __str__(self):
        return f"Me llamo {self.__nombre}, tengo {self.__patas} patas y sueno así: {self.habla()}"