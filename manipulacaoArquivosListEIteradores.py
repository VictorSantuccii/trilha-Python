# =========================================
# 1. MANIPULAÇÃO DE ARQUIVOS EM PYTHON
# =========================================

# ▶️ Criando um novo arquivo e escrevendo conteúdo com open('arquivo.txt', 'w')
# 'w' = modo de escrita (write). Se o arquivo já existir, será sobrescrito!
arquivo = open("arquivo.txt", "w") 


# Escrevendo 3 linhas de texto no arquivo
arquivo.write("Linha 1: Olá, mundo!\n")
arquivo.write("Linha 2: Python é poderoso.\n")
arquivo.write("Linha 3: Manipulação de arquivos é útil.\n")


# Sempre feche o arquivo após escrever (evita travamentos ou vazamento de memória)
arquivo.close()


# ▶️ Agora vamos ler o conteúdo do arquivo com 'r' (read)
arquivo = open("arquivo.txt", "r")  # modo leitura


# Lê o conteúdo inteiro como uma única string
conteudo = arquivo.read()


print("\n🔹 Conteúdo completo do arquivo:")
print(conteudo)


arquivo.close()


# ▶️ Lendo linha por linha
arquivo = open("arquivo.txt", "r")
print("\n🔹 Lendo linha por linha:")


for linha in arquivo:
    print(">>", linha.strip())  # strip remove espaços e \n


arquivo.close()

# ▶️ Usando 'with open(...) as' para garantir que o arquivo seja fechado automaticamente
print("\n🔹 Usando Context Manager (with):")


with open("arquivo.txt", "r") as arquivo:
    for linha in arquivo:
        print(">>", linha.strip())


# ▶️ Adicionando mais conteúdo com o modo 'a' (append = adicionar)
with open("arquivo.txt", "a") as arquivo:
    arquivo.write("Linha 4: Essa linha foi adicionada sem apagar as outras.\n")


# ▶️ Lendo o arquivo em modo binário
with open("arquivo.txt", "rb") as arquivo:
    conteudo_binario = arquivo.read()
    print("\n🔹 Conteúdo em bytes:", conteudo_binario)


# ===================================
# 2. COMO FUNCIONA O RANGE()
# ===================================


print("\n🔹 Como funciona o range():")


# range(início, fim, passo) → fim não é incluso
print("range(0, 5):", list(range(0, 5)))  # [0, 1, 2, 3, 4]
print("range(2, 10, 2):", list(range(2, 10, 2)))  # [2, 4, 6, 8]


# range também é um gerador, então não gera todos os números de uma vez (economiza memória)



# ===================================
# 3. COMPREENSÕES (COMPREHENSIONS)
# ===================================



# ▶️ LIST COMPREHENSION — Criar listas de forma compacta


# [ x * x        for      x in range(5) ]
#     ↑           ↑       ↑
#  expressão   laço     sequência

# [ EXPRESSÃO     for ITEM in SEQUÊNCIA    if CONDIÇÃO (opcional) ]




print("\n🔹 List Comprehension:")

# Exemplo: lista de quadrados dos números de 0 a 9
quadrados = [x ** 2 for x in range(10)]
print("Quadrados de 0 a 9:", quadrados)


# Lista apenas com números pares (condição if)
pares = [x for x in range(20) if x % 2 == 0]  # Para cada X eu pego esse X num range de 0 a 19 e passo uma condicional de X dividido por 2 com o resto zero para descobrir os pares 
print("Números pares de 0 a 19:", pares)


# ▶️ SET COMPREHENSION — para criar conjuntos únicos
nomes = ["Ana", "João", "Ana", "Carlos", "João"]
nomes_unicos = {nome for nome in nomes}
print("Nomes únicos:", nomes_unicos)


#{ nome          for         nome in nomes }
#  ↑            ↑              ↑
# expressão   laço         sequência


# ▶️ DICT COMPREHENSION — criar dicionários de forma rápida
numeros = [1, 2, 3, 4]
quadrados_dict = {x: x ** 2 for x in numeros}
print("Dicionário de quadrados:", quadrados_dict)

#{ chave:valor       for        x in numeros } 
#    ↑     ↑         ↑              ↑
# x      x*x      laço         sequência




# ===================================
# 4. ITERADORES 
# ===================================

# ▶️ ITERADOR MANUAL com iter() e next()
print("\n🔹 Iteradores com iter() e next():")

lista = ["a", "b", "c"]
meu_iterador = iter(lista)  # Transforma a lista em iterador

print(next(meu_iterador))  # 'a'
print(next(meu_iterador))  # 'b'
print(next(meu_iterador))  # 'c'
# Se chamar next() mais uma vez: erro (StopIteration)

# ▶️ ENUMERATE - retorna índice + valor ao mesmo tempo
print("\n🔹 Usando enumerate():")

nomes = ["Maria", "Lucas", "Juliana"]
for indice, nome in enumerate(nomes):
    print(f"{indice}: {nome}")

# Um iterador é um objeto que sabe "dar o próximo valor" numa sequência.
# Ele implementa dois métodos especiais: __iter__() e __next__()

print("### Exemplo de ITERADOR customizado ###")

class Contador:
    def __init__(self, limite):
        self.limite = limite
        self.atual = 0

    def __iter__(self):
        # Retorna o próprio objeto como iterador
        return self

    def __next__(self):
        # Método que retorna o próximo valor
        if self.atual < self.limite:
            valor = self.atual
            self.atual += 1
            return valor
        else:
            # Quando acabar a sequência, deve levantar StopIteration
            raise StopIteration

contador = Contador(5)


# ---------------------------------------
# GERADORES
# ---------------------------------------

# Geradores são funções que geram valores sob demanda, usando 'yield' ao invés de 'return'
# Eles são mais fáceis de criar do que um iterador manual, e são eficientes em memória.

print("\n### Exemplo de GERADOR ###")

def contador_generator(limite):
    atual = 0
    while atual < limite:
        yield atual  # "pausa" a função e entrega o valor atual
        atual += 1

# Usando o gerador:
for numero in contador_generator(5):
    print(numero)  # 0, 1, 2, 3, 4

# ---------------------------------------
# COMO GERADORES FUNCIONAM POR DENTRO
# ---------------------------------------

print("\n### Funcionamento interno do gerador ###")

gen = contador_generator(3)

print(next(gen))  # 0 -> função executa até o primeiro yield
print(next(gen))  # 1 -> retoma após yield anterior até o próximo yield
print(next(gen))  # 2
# print(next(gen)) # Se descomentar, StopIteration é levantado porque acabou a sequência

# ---------------------------------------
# POR QUE USAR GERADORES?
# ---------------------------------------

print("\n### Por que usar geradores? ###")

# Imagine uma lista gigante - criar tudo na memória pode ser ruim
# Geradores criam um valor por vez, economizando memória

def gerador_infinito():
    n = 0
    while True:
        yield n
        n += 1

gen_inf = gerador_infinito()

print(next(gen_inf))  # 0
print(next(gen_inf))  # 1
print(next(gen_inf))  # 2

# Podemos iterar no gerador infinito até um limite com um for e break

print("\nIterando gerador infinito até 5:")
for num in gen_inf:
    print(num)
    if num >= 5:
        break

# ---------------------------------------
# FUNÇÕES BUILT-IN para iteradores e geradores
# ---------------------------------------

print("\n### Funções úteis com iteradores e geradores ###")

lista = [10, 20, 30]

it = iter(lista)  # transforma lista em iterador

print(next(it))  # 10
print(next(it))  # 20
print(next(it))  # 30
# print(next(it)) # Levanta StopIteration

# enumerate() retorna um iterador que gera pares (índice, valor)
print("\nUsando enumerate:")
for indice, valor in enumerate(['a', 'b', 'c']):
    print(indice, valor)

# ---------------------------------------
# EXEMPLO FINAL: GERADOR QUE FILTRA NÚMEROS PARES
# ---------------------------------------

def pares_ate(limite):
    for numero in range(limite):
        if numero % 2 == 0:
            yield numero

print("\nPares até 10:")
for p in pares_ate(10):
    print(p)


# ▶️ GERADORES — funções que geram valores sob demanda usando `yield`

# Função geradora de números ao quadrado
def gerar_quadrados(limite):
    for x in range(limite):
        yield x ** 2  # yield "pausa" a função e retorna um valor por vez

print("\n🔹 Gerador de quadrados:")
for valor in gerar_quadrados(5):
    print("Quadrado:", valor)

# ▶️ Convertendo um gerador para lista
lista_gerada = list(gerar_quadrados(5))
print("Lista a partir do gerador:", lista_gerada)

# ▶️ GERADOR INFINITO com while True + yield
def contador_infinito():
    numero = 0
    while True:
        yield numero
        numero += 1

print("\n🔹 Gerador infinito controlado com break:")
for numero in contador_infinito():
    print("Número:", numero)
    if numero == 3:
        break  # interrompemos o loop

# ▶️ Gerador com lógica: apenas ímpares abaixo de 10
def gerar_impares():
    for i in range(10):
        if i % 2 == 1:
            yield i

print("\n🔹 Gerador de números ímpares:")
for impar in gerar_impares():
    print("Ímpar:", impar)
