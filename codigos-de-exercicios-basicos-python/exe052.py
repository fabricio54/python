# desenvolva um progama que leia o primeiro termo e a razão de uma pa. no final, mostre os 10 primeiros termos dessa progressão
termo = int(input("premeiro termo: "))
razao = int(input("razão: "))
pa = (termo + (10-1) * razao)
for i in range(termo, pa+razao, razao):
    print(f"{i}")
print()
print("resultado de uma pa!")