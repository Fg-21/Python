import math
class Punto:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    
    def __str__(self):
        return f"({self.__x}, {self.__y})"
        
    def setXY(self, newX, newY):
        self.__x = newX
        self.__y = newY

    def desplazaXY(self, dx, dy):
        self.__x += dx
        self.__y += dy

    def distancia(self, other):
        result = 0
        if isinstance(other, Punto):
            result =  math.sqrt((self.__x - other.__x)**2 + (self.__y - other.__y)**2)
        else:
            result = None
        return result
            
