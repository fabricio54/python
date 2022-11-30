# super progressão aritmética: pergunte ao usuário se ele que mostrar mais alguns termos

#pode ser desse jeito ou da outra maneira
'''ptermo = int(input('informe o primeiro termo: '))
razao = int(input('razão: '))
c = 0
num = -1
while num != 0:
    while c < razao:
        print(f'{ptermo}', end=' ')
        ptermo += razao
        c += 1
    print()
    num = int(input('quantos termos mais quer ver ? [0 para sair]'))
    if num != 0:
        razao = razao + num
print('fim...')'''

'''# segunda maneira
pt = int(input('informe o primeiro termo: '))
rz = int(input('informe a razão: '))
quant = int(input('quantidade de termos: '))
cont = 0
total = 0
while quant != 0:
    total += quant
    while cont < total:
        print(f'{pt}', end=' ')
        pt += rz
        cont += 1
    print()
    quant = int(input('quantos termos mais ? [0 para o progama encerrar]'))
print('fim...')'''