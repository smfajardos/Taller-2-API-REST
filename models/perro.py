from models.animal import Animal


class Perro(Animal):

    def __init__(self, nombre: str, peso: float, edad: int):
        super().__init__(nombre, peso, edad)

    def hacer_sonido(self):
        return "¡Guau, guau!"

    def comer(self, kilos: int):
        pass

    def get_kilos_comidos(self):
        pass
