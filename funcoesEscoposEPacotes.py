# ------------------------------------
# 10. FUNÇÕES EM PYTHON
# ------------------------------------

# Definindo uma função simples com 'def'
def saudacao():
    print("Olá! Seja bem-vindo(a)!")
saudacao()  # Chamada da função

# Função com parâmetros obrigatórios
def apresentar(nome, idade):
    print(f"Meu nome é {nome} e tenho {idade} anos.")
apresentar("Sant", 22)

# Parâmetros com valores padrão
def cumprimentar(nome="visitante"):
    print(f"Olá, {nome}!")
cumprimentar()           # Usa o valor padrão
cumprimentar("Bianca")   # Sobrescreve o valor padrão

# *args → argumentos variáveis posicionais (em forma de tupla)
def somar_todos(*numeros):
    total = sum(numeros)
    print(f"Soma total: {total}")
somar_todos(1, 2, 3, 4)

# **kwargs → argumentos nomeados variáveis (em forma de dicionário)
def mostrar_info(**dados):
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")
mostrar_info(nome="Victor", curso="ADS", idade=25)

# Função recursiva → chama ela mesma até atingir uma condição de parada
def fatorial(n):
    if n == 1:
        return 1
    return n * fatorial(n - 1)
print("Fatorial de 5:", fatorial(5))  # 5*4*3*2*1 = 120

# Funções lambda → funções anônimas (sem nome), usadas para expressões simples
dobro = lambda x: x * 2
print("Dobro de 7:", dobro(7))

# Funções de ordem superior → recebem funções como argumento ou retornam funções

# Exemplo: função que recebe outra função
def aplicar_operacao(valor, operacao):
    return operacao(valor)

print("Triplo usando função lambda:", aplicar_operacao(10, lambda x: x * 3))

# Exemplo: função que retorna outra função
def criar_saudacao(saudacao):
    def mensagem(nome):
        return f"{saudacao}, {nome}!"
    return mensagem

bom_dia = criar_saudacao("Bom dia")
print(bom_dia("Sant"))

# ------------------------------------
# 11. ESCOPO E VARIÁVEIS
# ------------------------------------

# Escopo local: a variável só existe dentro da função
def teste_local():
    x = 10  # escopo local
    print("Valor local de x:", x)
teste_local()
# print(x)  # Erro! x não está definido fora da função

# Escopo global: variável definida fora de todas as funções
x = 5

def teste_global():
    global x  # agora estamos modificando a variável global
    x = 20
    print("Dentro da função:", x)

teste_global()
print("Fora da função:", x)

# nonlocal → usado quando estamos dentro de uma função aninhada e queremos modificar uma variável da função externa (mas não global)
def externa():
    mensagem = "Olá"

    def interna():
        nonlocal mensagem
        mensagem = "Oi"
        print("Mensagem interna:", mensagem)

    interna()
    print("Mensagem externa:", mensagem)

externa()

# ------------------------------------
# 12. MÓDULOS E PACOTES
# ------------------------------------

# Módulo: arquivo .py com funções, classes ou variáveis reutilizáveis
# Suponha que temos um arquivo chamado 'util.py' com:

# --- util.py ---
# def somar(a, b):
#     return a + b
# ----------------

# Podemos importar e usar assim:
# from util import somar
# print(somar(2, 3))

# Outro exemplo com módulo interno do Python:
import math
print("Raiz quadrada de 25:", math.sqrt(25))
print("Pi com 5 casas decimais:", round(math.pi, 5))

# Podemos importar apenas uma função:
from math import factorial
print("Fatorial de 6:", factorial(6))

# Pacotes: diretórios que agrupam vários módulos (pastas com __init__.py dentro)
# Exemplo de estrutura:
# meu_pacote/
# ├── __init__.py
# ├── modulo1.py
# └── modulo2.py

# E no código:
# from meu_pacote.modulo1 import minha_funcao
# minha_funcao()
