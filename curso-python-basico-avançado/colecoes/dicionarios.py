"""     dicionarios

obs: Em algumas linguagens de progamação, os dicionários python são conhecidos por mapas

Dicionários são coleções do tipo chave/valor.

Dicionários são representados por chaves {}.

OBS:
    chave e valor são separados por dois pontos 'chave:valor':
    Tanto chave quanto valor podem ser qualquer tipo de dado:
    podemos misturar tipos de dodos:



# exemplo de dicionários:

# 1 forma
paises = {'br': 'Brasil', 'eua':'Estados Unidos', 'py': 'Paraguai'}

print(paises)
print(type(paises))

# 2 forma
paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguay')

print(paises)
print(type(paises))

# acessando elementos

# forma 1 - Acessando via chave, da mesma forma que lista/tupla
print(paises['br'])
print(paises['py'])
# print(paise['ru'])

# OBS: Caso tentamos fazer um acesso utilizando uma chave que não existe, teremos o erro keyErrer

# forma 2 - Acessando via get - Recomendada

print(paises.get('br'))
print(paises.get('ru'))

# fazendo uma busca pelos paises pela sua respectiva chave

pais = paises.get('br')

if pais:
    print(f'Encontrei o pais {pais}')
else:
    print(f'Não encontrei o país')

# fazendo testes logicos
print('br' in paises)
print('re' in paises)
print('Estados Unidos' in paises)

# podemos utilizar qualquer tipo de dado (int, float, string, boolean), inclusive lista, tupla dicionário, como chaves
# de dicionários

localidades = {

    (35.6895, 39.6917): 'Escritório em Tókio',
    (40.7128, 74.0060): 'Escritório em Nova York',
    (37.7749, 322.4194): 'Escritório em São Paulo',

}

#print(localidades)
#print(type(localidades))

# adicionando elementos em um dicionário

receita = {'jav': 100, 'fev': 120, 'mar': 300}

# forma 1

receita['abr'] = 350

print(receita)

# forma 2

novo_dado = {'mai': 500}

receita.update(novo_dado)
print(receita)

# atualizando dados em um dicionário

# forma 1

receita['mai'] = 550

print(receita)

# forma 2

receita.update({'mai': 800})

print(receita)

# conclusão 1: A forma de adicionar novos elementos ou atualizar dados em um dicionário é a mesma.
# conclusão 2: Não podemos ter chaves repetidas

# remover dados de um dicionário
# 1 forma
receita.pop('mar')  # removendo pela chave
# OBS: para removermos pelo metodo pop precisamos obrigatoriamente informar a chave
print(receita)
# 2 forma
del receita['fev']
print(receita)

# utilização de dicionarios

carrinho = []

produto1 = {'Produto': 'Relogio', 'quantidade:': 1, 'preco:': 2300.00}
produto2 = {'nome': 'God of War 4', 'quantidade': 1, 'preco': 150.00}

carrinho.append(produto1)
carrinho.append(produto2)

# print(carrinho)

# métodos de dicionários

d = dict(a=1, b=2, c=3)
print(d)
print(type(d))

# limpar o dicionário (Zerar dados)
#d.clear()
#print(d)

# copiando um dicionário para outro
# forma 1
novo = d.copy()
print(novo)
novo['d'] = 4
print(d)
print(novo)

# forma não usual de criação de dicionários

outro = {}.fromkeys('a', 'b')  # desta forma criamos um dicionário com uma chave e um elemento

print(outro)
print(type(outro))

 Mapas -> conhecidos em python como dicionários
    Dicionários em python são representados por chaves
    """

ganho = {'jan': 100, 'fev': 250, 'mar': 400}

# interagir sobre dicionários
for chave in ganho:
    print(chave)

for chave in ganho:
    print(ganho[chave])

for chave in ganho:
    print(f'{chave}: {ganho[chave]}')

# maneira mais pytônica de se trabalhar
for chave in ganho.keys():
    print(ganho[chave])      # acessando as chaves

# acessando os valores

print(ganho.values())

# desempacotamento de dicionários
print(ganho.items())

for chave, valor in ganho.items():
    print(f'chave={chave} e valor={valor}')
