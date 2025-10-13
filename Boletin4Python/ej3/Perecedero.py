from Boletin4Python.ej3 import Producto


class Perecedero(Producto):
    def __init__(self, nombre, precio, dias_a_caducar):
        super().__init__(nombre, precio)
        self.__dias_a_caducar = dias_a_caducar

    def calcular(self, cantidad):
        total = super().calcular(cantidad)
        if self.__dias_a_caducar == 1:
            total /= 4
        elif self.__dias_a_caducar == 2:
            total /= 3
        elif self.__dias_a_caducar == 3:
            total /= 2
        return total

    def __str__(self):
        return f"{self._Producto__nombre} - Precio: {self._Producto__precio:.2f} - Días a caducar: {self.__dias_a_caducar}"