#Cree una clase Vehículo que contenga los atributos de instancia velocidad_maxima y kilometraje

class Vehiculo:
    def __int__(self, vel_maxima: str, kilometraje: float):
        self.vel_maxima: str = vel_maxima
        self.kilometraje: float = kilometraje