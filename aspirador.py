import random

class Aspirador():
    def __init__(self):
        self.arg = arg
        self.posicao_x = randint(0, 8)
        self.posicao_y = randint(0, 8)


class Casa():
    def __init__(self):
        self.limpo = random.choice([True, False])

    def limpa(self):
        self.limpo = False

    def suja(self):
        self.limpo = True


def main():
    Aspirador()

    mapa = {}

    for row in range(0,8):
        mapa[row] = {}
        for col in range(0,8):
            mapa[row][col] = Casa()

    print(mapa[0][0].limpo)


if __name__ == '__main__':
    main()
