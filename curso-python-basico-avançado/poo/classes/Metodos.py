"""
POO - Métodos

- Métodos (funções) -> Representam os comportamentos do objeto. Ou seja, as ações que este objeto pode realizar no seu sistema.

Em Python, dividimos os métodos, assim como os atributos, em 2 grupos: Métodos de instância e Métodos de Classe.

# Métodos de Instância

# O método dunder init__init__ é um método especial chamado de construtor e sua função é construir o objeto a partir da classe.

OBS: Todo elemento em Python que inicia e finaliza com underline é chamado do dunder (Double Underline)

OBS: Os métodos/funções dunder em Python são chamados de métodos mágicos.

ATENCÃO: Por mais que possamos criar nossas próprias funções utilizando dunder (underline no início e no fim) não é aconselhado. Python possui vários métodos com esta forma de nomenclatura e pode ser que mudemos o corpotamento dessas funções mágicas internas da linguagem. Então, evite ao máximo. De preferência nunca o faça.
"""

class Lampada:
    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero

class Produto:
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        """Retorna o valor do produto com o desconto"""
        return (self.__valor * (100 - porcentagem)) / 100

class Usuario:
    # Atributo estatico da classe
    contador = 0;

    # decoration
    @classmethod
    def conta_usuarios(cls):
        print(f'Temos {cls.contador} usuários no sistema')

    def __init__(self, nome, sobrenome ,email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def __gera_usuario(self):
        return self.__email.split('')

usu = Usuario("Carlos", "Alberto", "Carlosgabas@gmail.com", 3434)
usu2 = Usuario("Maria", "Augusta", "Mariaaugusta@gmail.com", 2353)

print(usu.nome_completo())
print(usu2.nome_completo())



produto = Produto('PlayStation 4', 'Video Game', 2500)
print(produto.desconto(10))


   