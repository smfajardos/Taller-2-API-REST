from abc import ABC, abstractmethod


class IAnimal(ABC):

    @abstractmethod
    def comer(self, kilos: int):
        pass

    @abstractmethod
    def get_kilos_comidos(self):
        pass
