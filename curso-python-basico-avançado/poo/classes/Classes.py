""" 
POO - Classes

Em POO, Classes nada mais são do que modelos dos objetos do mundo real sendo representados computacionalmente.

Imagine que você queira fazer um sistema para automatizar o controle das lâmpadas da sua casa.

Classes podem conter:

    - Atributos -> Representam as caracteristicas dos objetos. Ou seja, pelos atributos conseguimos representar computacionalmente os estados de um objeto. No caso da lâmpada, possivelmente iriamos querer saber se a lâmpada é 110 ou 220 volts. se ela é branca, amarelo, vermelha ou outra cor, qual é a luminosidade dela e etc.

    Em Python, dividimos os atributos em 3 grupos:
        - Atributos de Instância;
        - Atributos de Classe;
        - Atributos Dinâmicos;

    # Atributos de instância: São atributos declarados dentro do método construtor.

    # OBS: Método construtor: é um método especial utilizado para a construção do objeto.

    # Em Java, uma classe Lâmpada, incluindo seus atributos ficaria seus atributos ficaria mais ou menos:

    public class Lampada(){
        
        private int voltagem;
        private String cor;
        private Boolean ligado = false;

        public Lampada(int voltagem, String cor){
            this.voltagem = voltagem;
            this.cor = cor;
        }
    }

    - Métodos (funções) -> Representam os comportamentos do objeto. Ou seja, as ações que este objeto pode realizar no seu seu sistema. No caso da lâmpada, por exemplo, um comportamento comum que muito provavelmente iriamos querer representar no nosso sistema é o de ligar e desligar a mesma.

Em python para definir uma classe utilizam a palavra reservada class.

OBS: Utilizamos a palavra 'pass' em python quando temos um bloco de código que ainda não está implementado.

OBS: Quando nomeamos nossas classes em Python utilizamos por convenção o nome com inicial em maiúscula, todas juntas.

Em Python, por convenção, ficou estabelicido que todo atributo de uma classe é público.
Ou seja, pode ser acessado em todo o projeto.
Caso queiramos demostrar que determinado atributo deve ser tratado como private, ou seja, que deve ser acessado/utilizado somente dentro de própria classe está declarado, autiliza-se __ duplo underscore no início de seu nome.

Isso é conhecido também com Name Mangling.

"""
# classes como atributos públicos

class Lampada:
    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligado = False

class ContaCorrente:
    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo
    
class Produto:

    # Atributos de Classe
    imposto = 1.05 # 0.05% de imposto
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id

class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

# classes com atributos privados

class Acesso:
    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    # OBS: Lembre-se que isso é apenas uma convenção, ou seja, a linguagem Python não vai impedir que façamos acesso aos atributos sinalizadores como privados fora da classe.

    # Exemplo

# user = Acesso('user@gmail.com', '13424')
# print(user.email)
# print(user.senha)

p1 = Produto('PlayStation 5', 'Video Game', 3000)
p2 = Produto('Xbox One 5', 'Video Game', 3200)

print(p1.valor) # Acesso possível, mais não correto
print(p2.valor)

# OBS: Não precisamos criar uma instância de uma classe para fazer acesso a um atributo de classe

print(Produto.imposto) # Acesso correto de atributo de classe
print(p1.id)
print(p2.id)

# OBS: Em linguagens como o Java, os atributos conhecidos como atributos de classe aqui em Python
# são chamados de atributos estáticos;

# criação de atributos dinâmicos: criados em tempo de execução

p1.codigo = 123432

print(f'Produto: {p1.nome}, Descrição: {p2.descricao}, Valor: {p1.valor}, codigo: {p1.codigo}')





    

