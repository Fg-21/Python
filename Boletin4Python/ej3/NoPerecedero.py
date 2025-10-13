from Boletin4Python.ej3 import Producto


class NoPerecedero(Producto):
    def __init__(self, nombre, precio, tipo):
        super().__init__(nombre, precio)
        self.__tipo = tipo

    def __str__(self):
        return f"{self._Producto__nombre} - Precio: {self._Producto__precio:.2f} - Tipo: {self.__tipo}"