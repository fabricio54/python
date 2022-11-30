""" faça um progama que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista"""

"""val = []
maior = menor = 0

# temos duas maneiras de fazer os laços de repetição

# 1 forma
for i in range(0, 5):
    val.append(int(input(f'valor {i}: ')))
"""

val = [0] * 5
maior = menor = 0
# 2 forma
for i in range(0, 5):
    val[i] = int(input(f'valor {i}: '))

for i in range(0, 5):
    if i == 0:
        maior = menor = val[i]
    else:
        if maior < val[i]:
            maior = val[i]
        if menor > val[i]:
            menor = val[i]
print(f'maior: {maior} pos:{val.index(maior)}\nmenor: {menor} pos:{val.index(menor)}\n')