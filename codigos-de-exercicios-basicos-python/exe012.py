# 12: faça um algoritmo que leia um preço de um produto e mostre seu novo preço com 5% de desconto.
produto = float(input('informe o preço do produto: R$'))
desconto = 0.95
preço = produto * desconto
print(f'o produto custava R${produto} reais com o desconto de 5% fica por R${preço} reais')