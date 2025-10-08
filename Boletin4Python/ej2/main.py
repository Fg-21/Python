from Empleado import Empleado
from Operario import Operario
from Directivo import Directivo
from Oficial import Oficial
from Tecnico import Tecnico

if __name__ == "__main__":
    op = Operario("Juan")
    dire = Directivo("Mar")
    of = Oficial("Alberto José")
    tc = Tecnico("Joanna")

    print(op)
    print(dire)
    print(of)
    print(tc)
