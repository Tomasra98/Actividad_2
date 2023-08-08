#Cree una clase Circulo que tenga las propiedades centro y radio, las cuales se inicializan con parámetros en el constructor. Defina métodos en la clase para calcular el área, el perímetro e indicar si un punto pertenece al círculo o no

from math import sqrt
from math import pi
class Círculo:
    def __init__(self, centro: float, radio: int):
        self.x1: int = int((centro * 10) // 10)
        self.y1: int = int((centro * 10) % 10)
        self.radio: int = radio

    def area(self) -> float:
        return pi * (self.radio)**2
    def perimetro(self) -> float:
        return 2 * pi * self.radio
    def punto_pertenece_al_ciculo(self, punto: float) -> bool:
        self.x2: int = int((punto * 10) // 10)
        self.y2: int = int((punto * 10) % 10)
        if((sqrt(self.x2 - self.x1)**2 + (self.y2 - self.y1)**2) <= self.radio):
            return True
        else:
            return False



MiCirculo = Círculo(2, 9.4)
print(MiCirculo.area())
print(MiCirculo.perimetro())
print(MiCirculo.punto_pertenece_al_ciculo(7.7))