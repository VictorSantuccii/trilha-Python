
tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

tuplaVazia = ()

tuplaStrings = ('Oi', 'Olá', 'Bom dia!')

primeiro = tuplaStrings[0]

print(primeiro)

ultimo = tuplaStrings[-1]

print(ultimo)

terceiro = tuplaStrings[2]

print(terceiro)

tamanho = len(tuplaStrings)
print(tamanho)

tupla1 = (1, 2, 3, 4, 5)
tupla2 = (6, 7, 8, 9, 10)

concatenacao = tupla1 + tupla2
print(concatenacao)

tuplaRepetida = (1, 2, 3, 4, 5)

repeticaoTupla = tuplaRepetida * 3
print(repeticaoTupla)


lista = ['Oi', 'Olá', 'Bom dia!', 'Oi', 'Oi']

if 'Oi' in lista:
    quantidade = lista.count('Oi')
    print(f"'Oi' aparece {quantidade} vezes.")
else:
    print("'Oi' não está na lista.")
    
    
    
tupla3 = ('Oi', 'Olá', 'Bom dia!')

indice = tupla.index('Olá')
print(f"O índice de 'Olá' é: {indice}")
    
    
    
tupla_vazia = ()

if not tupla_vazia:
    print("A tupla está vazia.")
else:
    print("A tupla NÃO está vazia.")

