# faça um programa que leia um vetor de caracteres de tamanho n, contendo as respostas de um candidato em uma prova de um curso. a seguir, leia outro vetor, dessa vez contendo o gabarito da prova. gere um terceiro vetor, de booleanos indicando os erros e acertos do canditatot. com base nesse vetor imprima o percentual de questões acertados pelo candidato.
def ler_vetor(lista, tam):
    for i in range(tam):
        lista[i] = str(input(f'questão {i+1}: [A/B/C/D/E]')).upper().strip()[0]

def correcao(aluno, gabarito, acertos, tam):
    for i in range(tam):
        if aluno[i] == gabarito[i]:
            acertos.append(aluno[i])
    return acertos

questoes = int(input('informe o número de questões da prova: '))
aluno = [0] * questoes
gabarito = [0] * questoes
respostas = []
print('respostas do canditato: ')
ler_vetor(aluno, questoes)
print('gabarito: ')
ler_vetor(gabarito, questoes)
correcao(aluno, gabarito, respostas, questoes)
porcentagem = len(respostas) * 100 / questoes
print(f'o candidato acertou {len(respostas)} questões e seu percentual de acertos foi {porcentagem:.2f}%')




