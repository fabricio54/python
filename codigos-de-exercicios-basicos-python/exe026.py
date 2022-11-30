# 26: faça um programa que leia uma frase pelo teclado e mostre:
# quantas vezes aparece a letra 'a'.
# em que posição ela aparece a primeira vez.
# em que posição ela aparece a última vez.
frase = str(input('digite uma frase qualquer pelo teclado: ')).lower().strip()
lista = frase.split()
junto = ''.join(lista)
print(f'a letra A aparece {junto.count("a")} vez(es).')
if 'a' in frase:
    print(f'a primeira letra A aparece na {junto.find("a")+1}º posição.')
    print(f'a ultima letra A aparece na {junto.rfind("a")+1}º posição.')