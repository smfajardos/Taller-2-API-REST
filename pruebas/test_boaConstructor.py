import unittest
from models.boaConstructor import BoaConstructor
from models.animalExotico import AnimalExotico
from models.iAnimal import IAnimal
from models.animal import Animal


class TestBoaConstructor(unittest.TestCase):

    def test_hacer_sonido(self):
        boaConstructor1 = BoaConstructor ("Boa", 5.5, 5, "Colombia", 17.5)
        self.assertEquals(boaConstructor1.hacer_sonido(), "¡Tsss!")

    def test_calcular_flete(self):
        boaConstructor1 = BoaConstructor ("Boa", 5.5, 5, "Colombia", 17.5)
        self.assertEquals(boaConstructor1.calcular_flete(), 96.25)

    def test_comer_ratones(self):
        boaConstructor1 = BoaConstructor ("Boa", 5.5, 5, "Colombia", 17.5)
        self.assertEquals(boaConstructor1.comer_ratones(10), 20)