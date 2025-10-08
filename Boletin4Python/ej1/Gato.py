from Animal import Animal


class Gato(Animal):
    def __init__(self, nombre, patas):
        super().__init__(nombre, patas)
    
    def habla(self):
        return "Miau"
    
    def __str__(self):
        return f"Soy un Gato. {super().__str__()}"