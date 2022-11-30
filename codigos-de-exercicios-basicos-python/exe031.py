# desenvolva um programa que pergunte a distância de uma viagem em km. calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200 km de R$0,45 para viagens mais longas.
km = float(input('informe a distância da viagem em km: '))
if km <= 200:
    valor = km * 0.5
else:
    valor = km * 0.45
print(f'sua viagem foi de {km}km e o total a pagar é {valor}')
