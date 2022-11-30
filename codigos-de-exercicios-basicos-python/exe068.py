# faça um programa que jogue par ou impar com o computador. o jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
from time import sleep

def par_ou_impar(j,c):
    cont = soma = 0
    while True:
        print('=-'*22)
        op = str(input('par ou impar ? [P/I]'))
        sleep(1)
        print('=-'*22)
        j = int(input('escolha um número de 1 a 10: '))
        print('minha vez...')
        sleep(1)
        c = randint(1, 10)
        soma = c + j
        print('=-'*22)
        if op in 'Pp':
            if soma % 2 == 1:
                print('você perdeu!')
                print(f'{c} + {j} = {soma}')
                return cont
            else:
                print('você ganhou!')
                print(f'{c} + {j} = {soma}')
        else:
            if soma % 2 == 0:
                print('você perdeu!')
                print(f'{c} + {j} = {soma}')
                return cont
            else:
                print('você ganhou!')
                print(f'{c} + {j} = {soma}')
        cont += 1



jogador = 0
computador = 0
vit = par_ou_impar(jogador, computador)
print(f'vc conseguiu ganhar {vit} vezes de mim.')
