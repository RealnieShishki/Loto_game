from Game import Game

if __name__ == '__main__':
    game = Game()
    while True:
        score = game.play_round()
        if score == 1:
            print('Вы выиграли')
            break
        elif score == 2:
            print('Вы проиграли')
            break