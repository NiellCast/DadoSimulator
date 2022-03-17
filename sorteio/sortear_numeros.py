from random import randint


class Dado:
    def __init__(self) -> None:
        self.__numero1 = None
        self.__numero2 = None

    @property
    def numero1(self) -> int:
        return self.__numero1

    @numero1.setter
    def numero1(self, sortear: bool) -> None:
        if sortear:
            self.__numero1 = randint(1, 6)

    @property
    def numero2(self) -> int:
        return self.__numero2

    @numero2.setter
    def numero2(self, sortear: bool) -> None:
        if sortear:
            self.__numero2 = randint(1, 6)
