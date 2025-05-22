# 🐍 GUIA DE IDENTAÇÃO EM PYTHON 🐍
# --------------------------------------
# Python usa indentação para definir blocos de código.
# Recomendado: 4 espaços por nível de indentação (PEP 8).
# NÃO use tabulação misturada com espaços.
# --------------------------------------

# ✅ CONDICIONAIS: if, elif, else



idade = 20

if idade >= 18:
    print("Você é maior de idade")  # Esse print está dentro do 'if'
else:
    print("Você é menor de idade")  # Esse print está dentro do 'else'






# ✅ LAÇOS DE REPETIÇÃO: for, while
for i in range(3):
    print("Laço for, número:", i)  # Está dentro do 'for'

contador = 0
while contador < 3:
    print("Laço while, contador:", contador)  # Está dentro do 'while'
    contador += 1






# ✅ FUNÇÕES: def
def saudacao(nome):
    # Tudo dentro da função deve ser indentado
    print(f"Olá, {nome}!")  # Está dentro da função

saudacao("Sant")






# ✅ CLASSES
class Pessoa:
    def __init__(self, nome):
        # self.nome é um atributo da instância
        self.nome = nome

    def dizer_ola(self):
        # Esse método pertence à classe
        print(f"Olá! Meu nome é {self.nome}")

p = Pessoa("Victor")
p.dizer_ola()






# ✅ ESTRUTURAS COMBINADAS: if dentro de for
for numero in range(5):
    if numero % 2 == 0:
        print(f"{numero} é par")
    else:
        print(f"{numero} é ímpar")





# ✅ BLOCO VAZIO: usar 'pass'
# Se você quiser deixar um bloco em branco por enquanto, use 'pass'
def futura_funcao():
    pass  # Isso evita erro de indentação até que você escreva o código depois

# ❌ ERRO COMUM: falta de indentação
# if True:
# print("Isso vai dar erro")  # ERRO! Está fora do bloco





# ✅ CORRETO:
if True:
    print("Isso está corretamente indentado")

# ✅ BOA PRÁTICA: múltiplos níveis de indentação
def exemplo_aninhado(x):
    if x > 0:
        for i in range(x):
            print(f"Valor: {i}")  # 3 níveis: função > if > for
    else:
        print("Valor inválido")

exemplo_aninhado(3)






# ✅ DICA FINAL:
# Use editores como VS Code ou PyCharm com indentação automática
# e extensões como 'Black' para formatar seu código com padrão profissional.

# ⚠️ Tabulação vs Espaços em Python

# No Python, a indentação pode ser feita com tabulação ou com espaços — 
# mas NÃO PODE misturar os dois no mesmo bloco. Isso gera erro de sintaxe.
