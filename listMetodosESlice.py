# 📚 MÉTODOS DE LISTAS EM PYTHON

# Lista de exemplo
frutas = ['maçã', 'banana', 'laranja']


# ✅ .append() → adiciona um item no final da lista
frutas.append('uva')  # ['maçã', 'banana', 'laranja', 'uva']


# ✅ .insert() → insere um item em uma posição específica
frutas.insert(1, 'morango')  # ['maçã', 'morango', 'banana', 'laranja', 'uva']


# ✅ .extend() → adiciona vários itens (concatena listas)
frutas.extend(['kiwi', 'melancia'])  # ['maçã', ..., 'melancia']


# ✅ .remove() → remove a primeira ocorrência do valor
frutas.remove('banana')  # Remove só a primeira 'banana' que encontrar


# ✅ .pop() → remove e retorna o último item (ou índice específico)
ultimo = frutas.pop()       # Remove 'melancia'
segundo = frutas.pop(1)     # Remove o item da posição 1


# ✅ .clear() → limpa todos os elementos da lista
# frutas.clear()  # Agora frutas = []


# ✅ .index() → retorna o índice do primeiro item com valor especificado
indice = frutas.index('laranja')  # Ex: retorna 2


# ✅ .count() → conta quantas vezes um valor aparece na lista
contagem = frutas.count('maçã')  # Ex: 1


# ✅ .sort() → ordena a lista **em ordem crescente** (altera a original)
numeros = [3, 1, 4, 2]
numeros.sort()  # [1, 2, 3, 4]


# ✅ .sort(reverse=True) → ordena em ordem decrescente
numeros.sort(reverse=True)  # [4, 3, 2, 1]


# ✅ .reverse() → inverte a ordem dos elementos (sem ordenar)
frutas.reverse()  # Inverte a lista atual


# ✅ .copy() → cria uma cópia da lista
frutas_copia = frutas.copy()


# ✅ len(lista) → retorna o tamanho da lista
tamanho = len(frutas)


# ✅ in → verifica se um item existe na lista
existe = 'uva' in frutas  # True ou False


# ✅ del lista[i] → remove o item pelo índice
del frutas[0]  # Remove o item na posição 0


# ✅ slicing (fatiamento)
sublista = frutas[1:3]  # Pega os itens do índice 1 até 2

# ----------------------------------------------------------------

# Lista de exemplo
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g']


# ✅ lista[início:fim] → pega do índice início até fim - 1
print(letras[0:3])   # ['a', 'b', 'c']


# ✅ lista[:fim] → do início até fim - 1
print(letras[:4])    # ['a', 'b', 'c', 'd']


# ✅ lista[início:] → do índice até o fim
print(letras[3:])    # ['d', 'e', 'f', 'g']


# ✅ lista[:] → cópia completa da lista
print(letras[:])     # ['a', 'b', 'c', 'd', 'e', 'f', 'g']


# ✅ lista[início:fim:passo] → fatiamento com passo indo de dois em dois ( 2 )
print(letras[1:6:2]) # ['b', 'd', 'f']


# ✅ passo negativo → inverte a lista
print(letras[::-1])  # ['g', 'f', 'e', 'd', 'c', 'b', 'a']


# ✅ índices negativos → contam de trás para frente
print(letras[-3:])   # ['e', 'f', 'g']
print(letras[:-2])   # ['a', 'b', 'c', 'd', 'e']


# ✅ usando slice() (opcional, mesmo efeito)
fatia = slice(2, 5)
print(letras[fatia])  # ['c', 'd', 'e']

