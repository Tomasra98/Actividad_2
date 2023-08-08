#Cree una clase Carta que contenga dos propiedades valor y pinta, las cuales son asignadas solo al momento de la construcción del objeto (se pasan como parámetros en el constructor). Defina 4 constantes que representan los nombres de las 4 pintas que puede tener una carta

class Carta:
    nombre1 = "1"
    nombre2 = "2"
    nombre3 = "3"
    nombre4 = "4"
    def __init__(self, valor: str, pinta:str ):
        self.valor:str = valor
        self.pinta:str = pinta