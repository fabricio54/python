# 07 faça um programa que leia duas notas de um aluno e mostre a a média aritmética
nota1 = float(input('primeira nota: '))
nota2 = float(input('segunda nota?: '))
media = (nota1 + nota2) / 2
print(f'o aluno obteve {nota1} na primeira nota e {nota2} na segunda nota e sua média foi {media:.2f}')