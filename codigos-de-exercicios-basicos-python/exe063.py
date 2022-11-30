# escreva um progama que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência de finobacci.
# ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8

# esse com while
'''quant = int(input('informe o tamanho da sequência de finobacci: '))
ant = 0
atual = 1
proximo = 1
cont = 0
print(f'{ant} {atual}', end=' ')
while cont < quant - 2:
    print(f'{proximo}', end=' ')
    ant = atual
    atual = proximo
    proximo = atual + ant
    cont += 1'''

# esse com for
'''qt = int(input('informe a quntidade de termos da sequência de fibonacci: '))
ant = 0
atual = 1
prox = ant + atual
print(f'{ant} {atual}', end=' ')
for i in range(0, qt-2, prox):
    print(f'{prox}', end=' ')
    ant = atual
    atual = prox
    prox = ant + prox'''