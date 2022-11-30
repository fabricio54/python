# 42: refaça o desafio 035 dos triângulos,acrescentando o recurso de mostrar que tipo de triângulo será formado:
# EQUILÁTERO:todos os lados iguais;
# ISÓSCELES:dois lados iguais, um diferente;
# ESCALENO:todos os lados diferentes.
l1 = float(input('comprimento da parte 1 do triângulo: '))
l2 = float(input('comprimento da parte 2 do triângulo: '))
l3 = float(input('comprimento da parte 3 do triângulo: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l2 + l1:
    print('com as medidas informadas temos a posibilidade de formar um triângulo')
    if l1 == l2 and l2 == l3:
        print('além do mais da para formar um EQUILÁTERO com todas as partes iguais.')
    elif l1 != l2 and l1 != l3 and l2 != l3:
        print('além do mais da para se formar um ESCALENO por ter todos os lados diferentes.')
    else:
        print('além do mais da para se formar um ISÓSCELES com pelos um dos três lados diferente.')
else:
    print('com as medidas informadas não da para se formar um triângulo.')