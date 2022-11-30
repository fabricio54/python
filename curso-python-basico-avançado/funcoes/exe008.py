# faça um programa que leia um vetor de inteiros. imprima separadamente os valores pares e os valores impares do vetor:
from random import randint
def ler_matriz(vetor, tam):
    for i in range(tam):
        vetor[i] = randint(1, 9)

def par_impar(vetor, tam, arma):
    for i in range(tam):
        if vetor[i] % 2 == 0:
            arma[0].append(vetor[i])
        else:
            arma[1].append(vetor[i])
    return arma
n = int(input('números de elementos do vetor: '))
vt = [0] * n
arm = [[], []]
ler_matriz(vt, n)
print(vt)
vt = par_impar(vt, n, arm)
print('vetor com seus pares e impares separados.')
print(vt)