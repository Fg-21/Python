
from Producto import Producto
from NoPerecedero import NoPerecedero
from Perecedero import Perecedero

if __name__ == "__main__":
    # Crear productos
    p1 = Perecedero("Leche", 2.0, 2)
    p2 = NoPerecedero("Arroz", 1.5, "Grano")
    p3 = Producto("Galletas", 1.0)

    # Calcula precios
    print(p1.calcular(6))  
    print(p2.calcular(6)) 
    print(p3.calcular(6))  

    # Muostra info
    print(p1)
    print(p2)
    print(p3)

    # Compara productos
    print(p1 < p2)