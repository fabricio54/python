from time import sleep

def criando_vertices(tam, nomes):
    for i in range(0, tam, 1):
        nomes.append(str(input(f'nome do vertice {i + 1}: ')))


def definindo_ligacoes(lig, tam, nome, lis):
    c = num = 0
    while c < tam:
        num = int(input(f'informe quantas ligacoes tem o vertice {nome[c]}: '))
        while num > tam or num < 0:
            print(f'informação invalida! o grafo tem {tam} verteces ')
            num = int(input(f'informe quantos ligações tem o vertice {nome[c]}: '))
        for i in range(0, num, 1):
            lis.append(str(input(f'vertice ({nomes[c]}) liga com: ')))
        lig.append(lista[:])
        lis.clear()
        c += 1
        print('salvando dados...')
        sleep(1)


def mostrando(lig, tam, nome, lis):
    for i in range(0, tam, 1):
        print(f'{nome[i]} =', end='')
        for j, l in enumerate(lig[i]):
            print(f' -> {l}', end='')
        print()
        sleep(1)


def mostrar_op(lig, nome):
    usu = 's'
    pos = 0
    while usu not in 'Nn':
        print('visualize o vertice')
        print('digite: ')
        for i in range(0, len(nome), 1):
            print(f'<<<{i}>>> ({nome[i]}) ')
        pos = int(input('qual a opção desejada?'))
        print(f'carregando dados do vertice ({nome[pos]})...')
        sleep(1)
        while pos > len(nome):
            print('opção inválida! tente novamente.')
            pos = int(input(f'escolha uma opção dentre as posiveis: {lig}'))
        print(f'{nome[pos]} = ', end='')
        for i, j in enumerate(lig[pos]):
            print(f'-> {j} ', end=' ')
        print()
        usu = str(input('quer continuar ? [S/N]'))
        print()

vertices = int(input('numero de vertices: '))
nomes = []
liga = []
lista = []
criando_vertices(vertices, nomes)
definindo_ligacoes(liga, vertices, nomes, lista)
print("-=" * 21)
print("              GRAFO DIRECIONADO    ")
print("-=" * 21)
mostrando(liga, vertices, nomes, lista)
mostrar_op(liga, nomes)