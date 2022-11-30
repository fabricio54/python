# 44: elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# -á vista dinheiro/cheque:10% de desconto;
# -a vista no cartão: 5% de desconto;
# -em até 2x no cartão: preço formal;
# -3x ou mais no cartão: 20% de juros.
def parcelamento(opção, produto):
    if opção == 1:
        print(f'compra feita à vista no cartão: produto era R${produto} e com desconto de 5% fica por R${produto*0.95:.2f}.')
    elif opção == 2:
        print(f'compra parcelada: fica 2x de  R${produto/2:.2f} com o preço total de R${produto}.')
    else:
        produto = produto * 1.20
        quant = int(input(f'quer parcelar em quantas vezes ?'))
        print(f'compra parcelada: fica por {quant}x de R${produto/quant:.2f} total de R${produto:.2f}')
produto = float(input('preço do produto: '))
print('''[ 1 ] á vista ou cheque;
[ 2 ] no cartão;''')
pagamento = int(input('escolha uma das opções: '))
if pagamento == 1:
    print(f'pagamento feito a vista: produto custava R${produto} com desconto de 10% fica por R${produto*0.90:.2f}')
else:
    print(f'''[ 1 ] á vista no cartão;
[ 2 ] em até 2 vezes no cartão;
[ 3 ] em até 3 vezes ou mais;''')
    op = int(input('escolha uma opção: '))
    parcelamento(op, produto)