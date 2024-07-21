from models.boaConstructor import BoaConstructor
from models.huron import Huron


def __init__(self, BoaConstructor: list, Huron:list):
        self.boas = [BoaConstructor(), BoaConstructor()]
        self.hurones = [Huron(), Huron()]


def alimentar_boa(self, boa_alimentar):
        try:
            boa1 = self.boas[boa_alimentar]
            if boa1 is None:
                return "La boa no existe!"
            else:
                boa1.comer_ratones()
                return "Comió con éxito"
        except IndexError:
            return "La boa no existe!"
        except ValueError:
            return "La boa está llena"
