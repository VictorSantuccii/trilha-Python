# ---------------------------------------------
# EXEMPLO DE USO DO range()
# ---------------------------------------------

# Forma mais básica: range(stop)
# Começa em 0, vai até 4 (o 5 não entra)
print("range(stop):")
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

print("\nrange(start, stop):")
# Começa em 2, vai até 6 (exclui o 6)
for i in range(2, 6):
    print(i)  # 2, 3, 4, 5

print("\nrange(start, stop, step):")  # step significa o passo em que vai andar, ou seja, de 2 em 2, 3 em 3
# Começa em 1, vai até 10, pulando de 2 em 2
for i in range(1, 10, 2):
    print(i)  # 1, 3, 5, 7, 9

print("\nrange decrescente:")
# Contagem decrescente: de 10 até 1, pulando de -1
for i in range(10, 0, -1):
    print(i)  # 10, 9, ..., 1

# ---------------------------------------------
# LIST COMPREHENSION
# ---------------------------------------------


print("\nList comprehension: quadrados de 0 a 4")
quadrados = [x * x for x in range(5)]
print(quadrados)  # [0, 1, 4, 9, 16]

print("\nList comprehension com if: apenas pares de 0 a 9")
pares = [x for x in range(10) if x % 2 == 0]
print(pares)  # [0, 2, 4, 6, 8]

print("\nList comprehension com operação de string:")
nomes = ["ana", "joão", "bia"]
maiusculos = [nome.upper() for nome in nomes]
print(maiusculos)  # ['ANA', 'JOÃO', 'BIA']


# ---------------------------------------------
# SET COMPREHENSION
# ---------------------------------------------


print("\nSet comprehension: eliminar duplicatas automaticamente")
nomes = ["ana", "joão", "ana", "maria"]
nomes_unicos = {nome for nome in nomes}
print(nomes_unicos)  # {'ana', 'joão', 'maria'}

print("\nSet comprehension com expressão:")
mod_3 = {x % 3 for x in range(10)}
print(mod_3)  # {0, 1, 2}


# ---------------------------------------------
# DICT COMPREHENSION
# ---------------------------------------------


print("\nDict comprehension: números e seus quadrados")
dicionario = {x: x * x for x in range(5)}
print(dicionario)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

print("\nDict comprehension com strings:")
nomes = ["ana", "bia", "carlos"]
tamanhos = {nome: len(nome) for nome in nomes}
print(tamanhos)  # {'ana': 3, 'bia': 3, 'carlos': 6}


# ---------------------------------------------
# EXPLICANDO OS PARÂMETROS DE range()
# ---------------------------------------------

print("\nrange(start, stop, step) - exemplo com valores visíveis:")
inicio = 1       # valor inicial da sequência
fim = 10         # valor final (não incluso)
passo = 2        # de quantos em quantos

for i in range(inicio, fim, passo):
    print(f"Início: {inicio}, Fim: {fim}, Passo: {passo} -> Valor: {i}")
