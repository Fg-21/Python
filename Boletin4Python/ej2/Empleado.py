class Empleado:
    def __init__(self, nombre = ""):
        self.__nombre = nombre

    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, newName):
        self.__nombre = newName

    def __str__(self):
        return f"Empleado: {self.getNombre()}"