# exercicio 34: escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.para salários superiores a R$1.250,00, calcule um aumento de 10% para os inferiores ou iguais, o aumento é de 15%.
salário = float(input('informe o seu salário: '))
if salário > 1250:
    aumento = salário * 1.10
    print(f'seu salário era de R${salário} com o aumento de 10% passou a ser R${aumento:.2f} ')
else:
    aumento = salário * 1.15
    print(f'seu salário era de R${salário} com o aumento de 15% passou a ser R${aumento:.2f}')