from Animal import Animal
class Perro(Animal):
    def __init__(self, nombre, patas):
        super().__init__(nombre, patas)
    
    def habla(self):
        return "Guau"
    
    def __str__(self):
        return f"Soy un Perro. {super().__str__()}"