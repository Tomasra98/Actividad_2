#Cree una clase Rectángulo la cual contiene dos atributos de instancia que representan los puntos que definen sus esquinas. Agregue métodos a la clase Rectángulo para calcular su perímetro, calcular su área e indicar si el rectángulo es un cuadrado

class Rectangulo:
    def __init__(self, punto1: float, punto2: float): #Se ingresan los datos como decimales
        self.x1: int = int((punto1*10)//10)
        self.y1: int = int((punto1*10)%10)
        self.x2: int = int((punto2*10)//10)
        self.y2: int = int((punto2*10)%10)
    def imprimir(self):
        print("(",self.x1,",",self.y1,")","\n","(", self.x2, ",", self.y2, ")")

    def determinar_mayor(self):
        if (self.x1 > self.x2):
            base = self.x1 - self.x2
        else:
            base = self.x2 - self.x1
        if (self.y1 > self.y2):
            altura = self.y1 - self.y2
        else:
            altura = self.y2 - self.y1

        return base, altura
    def perimetro(self) -> int:
        base, altura = self.determinar_mayor()

        return base*2 + altura*2

    def area(self) -> float:
        base, altura = self.determinar_mayor()
        return (base * altura)/2
    def det_cuadrado(self):
        base, altura = self.determinar_mayor()
        if(base - altura == 0 and base != 0 and altura != 0):
            return True
        else:
            return False



MiRectangulo = Rectangulo(0.9, 3.5)
MiRectangulo.imprimir()

print("Perimetro:",MiRectangulo.perimetro())
print("Area",MiRectangulo.area())
print("¿Es cuadrado?",MiRectangulo.det_cuadrado())