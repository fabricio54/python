# faça um programa que leia dois vetores e gere um terceiro vetor sendo a concotenação dos dois primeiros. não use a concatenação de listas do python.
def ler_vetor(vetor, tam):
    for i in range(tam):
        vetor[i] = int(input(f'elemento {i+1} do vetor: '))

def concatenar_vetor(vetorf, vetor1, vetor2, e1, e2):
    for i in range(e1):
        vetorf[i] = vetor1[i]
    for i in range(e2):
        vetorf[i+e1] = vetor2[i]

n1 = int(input('informe um número de elementos do primeiro vetor: '))
n2 = int(input('informe um número de elementos do segundo vetor: '))
vt = [0] * n1
vt2 = [0] * n2
vtfin = [0] * (n1+n2)
print('lendo o primeiro vetor: ')
ler_vetor(vt, n1)
print('lendo o segundo vetor: ')
ler_vetor(vt2, n2)
concatenar_vetor(vtfin, vt, vt2, n1, n2)
print('primeiro vetor: ')
print(vt)
print('segundo vetor: ')
print(vt2)
print('concotenação dos dois vetores: ')
print(vtfin)