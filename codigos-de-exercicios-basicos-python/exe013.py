# 13:faça um progama que leia um salário de um funcionário e o reajusto de 15% de aumento.
salario = float(input('informe seu salário: '))
reajuste = salario * 1.15
print(f'o funcionário recebia R${salario} e com um rejuste de 15% passará a receber R${reajuste:.2f}')