# crie um progama que leia o ano de nascimento de sete pessoas.no final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
ano = date.today().year
nasc = maior = menor = 0
for i in range(0, 7, 1):
    nasc = int(input("data de nascimento: "))
    if ano - nasc > 18:
        maior += 1
    else:
        menor += 1
print(f"{maior} pessoas já são maiores de idade!")
print(f"{menor} pessoas ainda menores de idade!")