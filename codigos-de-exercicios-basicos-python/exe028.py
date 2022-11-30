# 28: escreva un programa que faça o computador 'pensar' em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o númer escolhido pelo computador.o programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
print('='*40)
print(f'{"VAMOS JOGAR":^10}')
print('='*40)
computador = randint(0, 5)
num = int(input('estou pensando em um número de 0 a 5 adivinhe qual é ? '))
if num == computador:
    print(f'VOCÊ VENCEU!')
    print(f'o número que eu e você pensamos foi {num}')
else:
    print(f'VOCÊ PERDEU!')
    print(f'o número que eu pensei foi {computador} e você pensou pensou no {num} ')