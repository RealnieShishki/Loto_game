from Game import Game

if __name__ == '__main__':
    game = Game()
    while True:
        if game.comp_card() is True:
            print("Карточки отличаются")
        score = game.play_round()
        if score == 1:
            print('Вы выиграли')
            break
        elif score == 2:
            print('Вы проиграли')
            print(game)
            break

