import unittest
from models.huron import Huron
from models.animalExotico import AnimalExotico
from models.iAnimal import IAnimal
from models.animal import Animal


class TestHuron(unittest.TestCase):

    def test_hacer_sonido(self):
        huron1 = Huron ("Huron", 5.5, 5, "Colombia", 17.5)
        self.assertEquals(huron1.hacer_sonido(), "¡Eek Eek!")

    def test_calcular_flete(self):
        huron1 = Huron ("Boa", 5.5, 5, "Colombia", 17.5)
        self.assertEquals(huron1.calcular_flete(), 96.25)

