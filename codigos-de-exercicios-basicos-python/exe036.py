# exercicio 36: escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.a prestação mensal, não pode exceder 30% do salário ou então o empréstimo será negado.
valor_casa = float(input('valor do imovel: '))
salário = float(input('salário do comprador: '))
anos = int(input('em quantos anos você vai pagar a casa: '))
mensalidade = valor_casa / (anos*12)
sal = salário * 0.3
if mensalidade <= sal:
    print(f'\033[0;32mEMPRESTIMO APROVADO!\033[0m')
    print(f'o candidato está elegivel para o emprestimo')
else:
    print(f'\033[0;31mEMPRESTIMO NEGADO!\033[0m')
    print(f'o candidato não está elegivel para o emprestimo, a mensalidade teria que estar abaixo de 30% de seu salário sendo no máximo R${sal:.2f} ')