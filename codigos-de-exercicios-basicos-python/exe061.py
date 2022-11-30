# refaça o desafio 051. lendo o primeiro termo e a razaõ de uma pa, mostrando os 10 primeiros termos da progressão usando a estrutura while.

''' primeira exercicio maneira 1

ptermo = int(input('informe o primeiro termo: '))
razao = int(input('razão: '))
c = 0
while c < razao:
    print(f'{ptermo}', end=' ')
    ptermo += razao
    c += 1

'''


'''segundo exercicio maneira 2 função 

def PA(termo, razao, seq):
    if seq == 0:
        return termo
    return razao + PA(termo, razao, seq - 1)

pt = int(input('digite o primeiro termo: '))
rz = int(input('razão: '))
seq = int(input('informe a sequência: '))
res = PA(pt, rz, seq)
print(f'o resultado foi {res}')

'''