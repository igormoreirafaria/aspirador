import random
from random import randint

class Aspirador():
    def __init__(self):
        self.posicao_x = randint(0, 8)
        self.posicao_y = randint(0, 8)


    def move(self, arg):
        if(arg == 'direita'):
            if(self.posicao_x != 7):
                self.posicao_x = self.posicao_x + 1
            else:
                print('nao e possivel se mover pra direita')

        if(arg == 'baixo'):
            if(self.posicao_y != 7):
                self.posicao_y = self.posicao_x + 1
            else:
                print('nao e possivel se mover pra direita')

        if(arg == 'esquerda'):
            if(self.posicao_x != 0):
                self.posicao_x = self.posicao_x - 1
            else:
                print('nao e possivel se mover pra direita')

        if(arg == 'cima'):
            if(self.posicao_y != 0):
                self.posicao_y = self.posicao_y - 1
            else:
                print('nao e possivel se mover pra cima')




class Casa():
    def __init__(self):
        self.limpo = random.choice([True, False])

    def limpa(self):
        self.limpo = False

    def suja(self):
        self.limpo = True


def main():
    aspirador = Aspirador()

    mapa = {}

    for row in range(0,8):
        mapa[row] = {}
        for col in range(0,8):
            mapa[row][col] = Casa()



if __name__ == '__main__':
    main()
