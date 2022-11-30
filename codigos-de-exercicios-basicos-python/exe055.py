# faça um progama que leia o peso de cinco pessoas.no final, mostre qual foi o maior e o menor peso lidos.
tam = 5
peso = 0
maior = menor = 0
for i in range(0, tam, 1):
    peso = float(input('peso: '))
    if i == 0:
        maior = menor = peso
    elif maior < peso:
        maior = peso
    else:
        if menor > peso:
            menor = peso
print(f"o maior peso foi de {maior}")
print(f"o menor peso foi de {menor}")
