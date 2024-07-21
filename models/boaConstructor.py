from models.animalExotico import AnimalExotico
from models.iAnimal import IAnimal


class BoaConstructor(AnimalExotico, IAnimal):
    def __init__(self, nombre: str, peso: float, edad: int, pais_origen: str, impuestos: float):
        super().__init__(nombre, peso, edad, pais_origen, impuestos)
        self.ratones = 0
    
    def hacer_sonido(self):
        return "¡Tsss!"

    def comer_ratones(self, ratones: int):
        if self.ratones == 20:
            raise ValueError("Demasiados Ratones!")
        else:
            self.ratones += 1

    def get_kilos_comidos(self):
        return self.ratones
