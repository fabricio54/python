#desenvolva um progama que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.se o valor digitado for impar desconside-o

soma = 0
vetor = []
for i in range(0, 6, 1):
    vetor.append(int(input(f'elemento do vetor na pos {i+1}: ')))

print(f"o vetor e formado por 6 elementos e eles são {vetor}")
