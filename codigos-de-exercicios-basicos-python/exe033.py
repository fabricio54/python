# exercicio 33: faça um programa que leia três números e mostre qual é o maior e qual é o menor.
n1 = int(input('informe um número: '))
n2 = int(input('informe outro número: '))
n3 = int(input('informe o ultimo número: '))
if n1 > n2 and n1 > n3:
    maior = n1
    if n2 < n3:
        menor = n2
    else:
        menot = n3
elif n2 > n1 and n2 > n3:
    maior = n2
    if n1 < n3:
        menor = n1
    else:
        menor = n3
else:
    maior = n3
    if n1 < n2:
        menor = n1
    else:
        menor = n2
print(f'o maior número digitado foi {maior} e o menor {menor}')
