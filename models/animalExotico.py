from models.animal import Animal


class AnimalExotico(Animal):
    def __init__(self, nombre: str, peso: float, edad: int, pais_origen: str, impuesto: float):
        super().__init__(nombre, peso, edad)
        self.__pais_origen = pais_origen
        self.__impuesto = impuesto

    def get_pais_origen(self):
        return self.__pais_origen

    def get_impuesto(self) -> float:
        return self.__impuesto

    def calcular_flete(self) -> float:
        return self.__impuesto * self.get_peso()

    def hacer_sonido(self):
        pass

    def comer(self, kilos: int):
        pass

    def get_kilos_comidos(self):
        pass
