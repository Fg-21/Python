class CuentaCorriente:    
    def __init__(self, dni, saldo, nombre = ""):
        self.__dni = dni
        self.__saldo = saldo
        self.__nombre = nombre
    
    #getters

    def get_dni(self):
        return self.__dni
    
    def get_saldo(self):
        return self.__saldo

    def get_nombre(self):
        return self.__nombre
    
    #methods

    def sacarDinero(self, cantidad):
        sacado = False
        if self.__saldo >= cantidad:
            self.__saldo -= cantidad
            sacado = True
        return sacado

    def ingresa(self, cantidad):
        self.__saldo += cantidad

    def __str__(self):
        return f"Propietario: {self.__nombre}, con DNI: {self.__dni}" \
        "Saldo: {self.saldo}"
    
    def __eq__(self, other):
        equals = False
        if isinstance(other, CuentaCorriente):
            equals = self.__dni == other.get_dni()
        return equals
    
    def __lt__(self, other):
        return self.__saldo > other.get_saldo()
    