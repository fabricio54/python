""" crie um progama onde o usuário possa digitar vários valores númericos e cadastre-os em uma lista.
 Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
"""

val = []
num = cont = 0
usu = 's'
existe = False
while usu in 'Ss':
    num = int(input('informe um número: '))
    if cont == 0:
        val.append(num)
    else:
        for i in range(0, len(val)):
            if val[i] == num:
                existe = True
        if existe == False:
            val.append(num)
    existe = False
    cont += 1
    usu = str(input('quer continuar ?'))
print(val)