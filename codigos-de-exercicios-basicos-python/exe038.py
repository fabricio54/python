# 38: escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#-o primeiro valor é maior;
#-o segundo valor é maior;
#não existe valor maior, os dois são iguais.
num1 = int(input('primeiro número: '))
num2 = int(input('segundo número: '))
if num1 > num2:
    print(f'o número {num1} é maior que o {num2}.')
elif num2 > num1:
    print(f'o número {num2} é maior que o {num1}.')
else:
    print('os dois números são iguais.')