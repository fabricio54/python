# 45: crie um programa que faça o computador jogar jokenpô com você.
from random import randint
from time import sleep
computador = randint(0, 2)
print('''suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA ''')
op = int(input('qual é a sua opção ?'))
print('JO!')
sleep(1)
print('KEN!')
sleep(1)
print('PO!')
sleep(1)
if op == computador:
    print('você ganhou! joguei ', end='')
    if op == 0:
        print('PEDRA.')
    elif op == 1:
        print('PAPEL.')
    else:
        print('TESOURA.')
else:
    print('você perdeu! joguei ', end='')
    if computador == 0:
        print('PEDRA.')
    elif computador == 1:
        print('PAPEL.')
    else:
        print('TESOURA.')
