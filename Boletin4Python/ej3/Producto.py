class Producto:
    def __init__(self, nombre, precio):
        self.__nombre = nombre
        self.__precio = precio

    def calcular(self, cantidad):
        return self.__precio * cantidad

    def __str__(self):
        return f"{self.__nombre} - Precio: {self.__precio:.2f}"

    def __lt__(self, otro):
        return self.__precio < otro.__precio