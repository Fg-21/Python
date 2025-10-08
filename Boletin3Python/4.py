class Articulo:
    IVA = 21

    def __init__(self, nombre, precio, stock):
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock

    def getPVP(self):
        return self.__precio * Articulo.IVA/100 + self.__precio

    def getPVPDescuento(self, disscount):
        return self.getPVP() - self.getPVP() * (disscount/100)
    
    def sell(self, quantity):
        sellable = False
        if self.__stock > quantity:
            self.__stock -= quantity
            sellable = True
        return sellable
    
    def store(self, quantity):
        self.__stock += quantity
    
    def __str__(self):
        return f"Artículo: {self.__nombre}      Precio: {self.__precio}     Stock: {self.__stock}"
    
    def __eq__(self, other):
        if isinstance(other, Articulo):
            equals = self.__nombre == other.__nombre
        else:
            equals = None
        return equals 
    
    def __lt__(self, other):
        if isinstance(other, Articulo):
            result = self.__nombre < other.__nombre
        else:
            result = None
        return result 
