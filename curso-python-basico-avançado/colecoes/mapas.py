""" Mapas -> Conhecidos em Python como Dicionarios

Dicionàrios em python são representados por chaves {}

receita = {'jan': 100, 'fev': 250, 'mar': 400}
# Interar sobre dicionários
for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

print(receita.keys())

# Acessando chaves
for chave in receita.keys():
    print(receita[chave])

print(receita.values())

# Acessando os valores
for valor in receita.values():
    print(valor)

# Desempacotamento de Dicionários
for chave, valor in receita.items():
    print(f'chave={chave} e valor={valor}')

# soma', Valor Máximo, Valor Mínimo', Tamanho

# ' Se os valores forem todos inteiros ou reais

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))
"""

receita = {'jan': 100, 'fev': 250, 'mar': 400}

# soma', Valor Máximo, Valor Mínimo', Tamanho

# ' Se os valores forem todos inteiros ou reais

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))
