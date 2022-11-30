# melhore o jogo do desafio 028 onde o computador vai "pensar" em um número entre 0 e 10.só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
from time import sleep
cont = 0
print('vamos jogar o jogo da adivinhação!')
print('-='*22)
print('o computador vai pensar em um número agora! ')
sleep(1.5)
print('-='*22)
computador = randint(0, 10)
jogador = int(input('tente adivinhar o número?'))
while computador != jogador:
    cont += 1
    print('-='*22)
    print('VOCÊ ERROU! tente novamente.')
    print('computador pensando...')
    sleep(1.5)
    computador = randint(0, 10)
    print('-='*22)
    jogador = int(input('tente adivinhar novamente?'))
print('-='*22)
print(f'VOCÊ GANHOU! você jogou {jogador} e o computador {computador}')
print(f'precisou de {cont} vezes para me vencer!')
