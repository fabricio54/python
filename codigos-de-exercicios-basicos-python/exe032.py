# exercicio 32: faça um programa que leia um ano qualquer e mostre se ele é bissexto.
ano = int(input('informe um ano qualquer para vermos se ele é bissexto: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'o ano {ano} é bissexto!')
else:
    print(f'o ano {ano} não é bissexto!')