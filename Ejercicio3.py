#A la clase del punto anterior, defínale los siguientes métodos:
#- Un método mostrar que imprima por consola las coordenadas del punto
#- Un método mover que cambie las coordenadas del punto
# Un método calcular_distancia que calcule la distancia de la instancia actual con otro punto

from math import sqrt
class Punto:
    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y

    def imprimir(self):
        print("(", self.x, ",", self.y, ")")
    def mover(self, nuevo_x: int, nuevo_y: int):
        self.x = nuevo_x
        self.y = nuevo_y
    def calcular_distancia(self, punto: 'Punto') -> float:
        return sqrt((punto.x - self.x)**2 + (punto.y - self.y)**2)


if __name__ == "__main__":
    mipunto1 = Punto(3,1)
    mipunto2 = Punto(8, 13)

    mipunto1.imprimir()
    mipunto2.imprimir()

    mipunto1.mover(9,7)
    mipunto1.imprimir()

    print(mipunto1.calcular_distancia(mipunto2))