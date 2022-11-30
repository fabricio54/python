# crie um progama que leia uma frase qualquer e digo se ele é um palindrono, desconsiderando os espaços.

frase = str(input("escreva uma frase: ")).strip().upper()
dividir = frase.split()
palavra = ''.join(dividir)
tam = len(palavra)
aux = ''
for i in range(0, tam, 1):
    aux += palavra[tam-1-i]
if palavra == aux:
    print(f"a frase ao contrario é palindrono!")
    print(f"a palavra {palavra} ao contrario é {aux}")
else:
    print("a palavra não é palidrono!")
    print(f"a palavra {palavra} ao contrario é {aux}")