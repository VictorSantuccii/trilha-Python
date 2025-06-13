# -----------------------------------------
# 17. CLASSES E OBJETOS
# -----------------------------------------

# Definindo uma classe Pessoa
class Pessoa:
    # Construtor (__init__): chamado quando criamos um objeto
    def __init__(self, nome, idade):
        self.nome = nome        # atributo de instância
        self.idade = idade      # atributo de instância

    # Método normal: imprime informações
    def apresentar(self):
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."

    # Método mágico __str__: controla o que é mostrado quando printamos o objeto
    def __str__(self):
        return f"Pessoa({self.nome}, {self.idade})"

    # Método mágico __repr__: representação oficial, usada no console e debugger
    def __repr__(self):
        return f"Pessoa(nome={self.nome!r}, idade={self.idade!r})"

    # Método mágico __add__: podemos definir como somar pessoas, por exemplo
    def __add__(self, outra):
        # soma as idades, cria nova Pessoa com nome combinado
        novo_nome = f"{self.nome} & {outra.nome}"
        nova_idade = self.idade + outra.idade
        return Pessoa(novo_nome, nova_idade)

# Criando objetos
p1 = Pessoa("Sant", 25)
p2 = Pessoa("Bibizinha", 23)

print(p1.apresentar())  # método normal
print(p2)               # chama __str__

# Usando método mágico __add__
p3 = p1 + p2
print(p3)               # Pessoa combinada

# -----------------------------------------
# HERANÇA, POLIMORFISMO E ENCAPSULAMENTO
# -----------------------------------------

# Subclasse Estudante herda Pessoa
class Estudante(Pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)  # chama o construtor da superclasse
        self.curso = curso              # atributo extra


    # Polimorfismo: método apresentar diferente
    def apresentar(self):
        return f"Olá, sou {self.nome}, tenho {self.idade} anos e estudo {self.curso}."
    

# Encapsulamento (convenção: _atributo indica "privado")
class Banco:
    def __init__(self, saldo_inicial):
        self._saldo = saldo_inicial  # "privado", não acessar direto fora da classe


    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor


    def sacar(self, valor):
        if 0 < valor <= self._saldo:
            self._saldo -= valor


    def mostrar_saldo(self):
        return self._saldo
    

# Testando herança e polimorfismo
est = Estudante("Ana", 20, "Engenharia")
print(est.apresentar())  # chama método sobrescrito


# Testando encapsulamento
conta = Banco(1000)
conta.depositar(500)
conta.sacar(300)
print("Saldo atual:", conta.mostrar_saldo())


# -----------------------------------------
# 18. PROPRIEDADES E DESCRITORES
# -----------------------------------------

# Propriedade: controla acesso a atributo com getter e setter

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self._preco = preco  # atributo "privado"


    @property
    def preco(self):
        # Getter: chamado quando acessamos produto.preco
        return self._preco
    

    @preco.setter
    def preco(self, valor):
        # Setter: controla alteração do preço
        if valor < 0:
            raise ValueError("Preço não pode ser negativo")
        self._preco = valor


prod = Produto("Caneta", 2.5)
print(prod.preco)  # acessa getter


prod.preco = 3.0   # altera usando setter
print(prod.preco)

# prod.preco = -10 # isso causaria erro

# Descritor: um objeto que controla acesso a atributo
# Vamos criar um descritor simples que valida idade

class ValidadorIdade:
    def __get__(self, instance, owner):
        return instance._idade

    def __set__(self, instance, valor):
        if valor < 0 or valor > 120:
            raise ValueError("Idade inválida")
        instance._idade = valor

class Pessoa2:
    idade = ValidadorIdade()  # atributo descritor

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade   # isso chama ValidadorIdade.__set__

pessoa = Pessoa2("João", 30)
print(pessoa.idade)

# pessoa.idade = -5  # geraria erro ValueError

# -----------------------------------------
# 19. MÉTODOS ESTÁTICOS E DE CLASSE
# -----------------------------------------

class Matematica:
    @staticmethod
    def somar(a, b):
        # Método estático: não usa self nem cls
        return a + b

    contador = 0

    @classmethod
    def incrementar_contador(cls):
        # Método de classe: recebe a classe como primeiro parâmetro (cls)
        cls.contador += 1
        return cls.contador

print("Soma estática:", Matematica.somar(5, 7))

print("Contador antes:", Matematica.contador)
print("Contador depois:", Matematica.incrementar_contador())
print("Contador depois:", Matematica.incrementar_contador())

# -----------------------------------------
# 20. DECORADORES
# -----------------------------------------

# Decorador simples que imprime antes e depois da função decorada

def meu_decorador(func):
    def wrapper(*args, **kwargs):
        print("Antes da função")
        resultado = func(*args, **kwargs)
        print("Depois da função")
        return resultado
    return wrapper

@meu_decorador
def diz_ola():
    print("Olá!")

diz_ola()

# Decorador que adiciona repetição

def repetir_vezes(n):
    def decorador(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorador

@repetir_vezes(3)
def fala_bom_dia():
    print("Bom dia!")

fala_bom_dia()

# Decorador para classe (exemplo simples que adiciona método)

def decorador_classe(cls):
    cls.novo_metodo = lambda self: "Método adicionado via decorador"
    return cls

@decorador_classe
class MinhaClasse:
    def original(self):
        return "Método original"

obj = MinhaClasse()
print(obj.original())
print(obj.novo_metodo())
