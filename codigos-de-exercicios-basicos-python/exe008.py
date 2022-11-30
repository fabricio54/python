# 08 crie um progama que leia um valor em metros e escreva-o em centimétros e milímetros
valor = float(input('digite um valor em metros: '))
ct = valor * 100
ml = valor * 1000
print(f'{valor}m convertido em centímetros é {ct}cm e em milímetros {ml}ml')