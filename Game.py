from Gen_uniq_num import generate_unique_numbers
from Card import Card

class Game:
    __usercard = None
    __compcard = None
    __numkegs = 90
    __kegs = []
    __gameover = False

    def __init__(self):
        self.__usercard = Card()
        self.__compcard = Card()
        self.__kegs = generate_unique_numbers(self.__numkegs, 1, 90)

    def __str__(self):
        return f"осталось {len(self.__kegs)} бочонков"

    def comp_card(self):
        return self.__usercard != self.__compcard

    def play_round(self) -> int:
        """
        :return:
        0 - игра продолжается
        1 - игрок выиграл
        2 - компьютер выиграл

        """

        keg = self.__kegs.pop()
        print(f'Новый бочонок: {keg} (осталось {len(self.__kegs)})')
        print(f'----- Ваша карточка ------\n{self.__usercard}')
        print(f'-- Карточка компьютера ---\n{self.__compcard}')

        useranswer = input('Зачеркнуть цифру? (y/n)').lower().strip()
        if useranswer == 'y' and not keg in self.__usercard or \
           useranswer != 'y' and keg in self.__usercard:
            return 2

        if keg in self.__usercard:
            self.__usercard.cross_num(keg)
            if self.__usercard.closed():
                return 1
        if keg in self.__compcard:
            self.__compcard.cross_num(keg)
            if self.__compcard.closed():
                return 2

        return 0

