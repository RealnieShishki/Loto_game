import random


class Keg:
    __num = None

    def __init__(self):
        self.__num = random.randint(1, 90)

    @property
    def num(self):
        return self.__num

    def __str__(self):
        return str(self.__num)