"""crie um progama onde o usuário possa digitar cinco valores númericos e cadastreo-os ja na ordem certa sem usar o sort, no final mostre a ordem certa"""


'''
# metodo sem o append

val = [0] * 5
num = aux = 0
for i in range(0, 5):
    num = int(input('informe um número: '))
    
    val[i] = num
    for j in range(0, len(val)-1, 1):
        if val[j] > val[i]:
            aux = val[j]
            val[j] = val[i]
            val[i] = aux
print(f'a lista ordenada ficou {val}')
'''
# metodo sem o append

val = []
num = aux = 0

for i in range(0, 5):
    num = int(input('informe um número: '))
    val.append(num)
    for j in range(0, len(val)-1):
        if val[j] > val[i]:
            aux = val[j]
            val[j] = val[i]
            val[i] = aux
print(f'a lista ordenada ficou {val}')

