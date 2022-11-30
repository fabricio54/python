# 20: o mesmo professor de desafio anterior quer sortear a ordem de apresentação de trablalhos dos alunos. faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle
n1 = str(input('primeiro aluno: '))
n2 = str(input('segundo aluno: '))
n3 = str(input('terceiro aluno: '))
n4 = str(input('quarto aluno: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('a ordem de apresentação será ')
print(f'{lista}')