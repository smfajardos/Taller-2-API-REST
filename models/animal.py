from abc import ABC, abstractmethod
from models.iAnimal import IAnimal


class Animal(IAnimal, ABC):
    def __init__(self, nombre: str, peso: float, edad: int):
        self.__nombre = nombre
        self.__peso = peso
        self.__edad = edad

    @abstractmethod
    def hacer_sonido(self):
        pass

    def get_nombre(self):
        return self.__nombre

    def get_peso(self):
        return self.__peso

    def get_edad(self):
        return self.__edad
