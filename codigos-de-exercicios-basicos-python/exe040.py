# 40:-média entre 5.0 e 6.9: recuperação;
# # -média crie um programa que leia duas nottas de um aluno e calcule sua média,mostrando uma mensagem no final, de acordo com a média atingida:
# -média abaixo de 5.0: reprovado;
#  entre 7.0 ou superior:aprovado.
n1 = float(input('primeira nota: '))
n2 = float(input('segunda nota: '))
média = (n1 + n2) / 2
if média < 5:
    print(f'a sua média foi {média:.1f} portanto reprovado!')
elif média >= 7:
    print(f'a sua média foi {média:.1f} portanto aprovado!')
else:
    print(f'a sua média foi {média:.1f} portanto recuperação!')