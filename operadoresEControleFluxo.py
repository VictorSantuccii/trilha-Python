# ------------------------------------
# 7. STRINGS EM PYTHON
# ------------------------------------

# Concatenação (juntar strings)
nome = "Victor"
sobrenome = "Santucci"
nome_completo = nome + " " + sobrenome
print("Concatenação:", nome_completo)



# Fatiamento (pegando pedaços da string)
texto = "Python é incrível"
print("Primeiros 6 caracteres:", texto[:6])  # 'Python'
print("Últimos 8 caracteres:", texto[-8:])   # 'incrível'



# F-strings (formatação moderna de strings)
idade = 25
print(f"Olá, meu nome é {nome} e tenho {idade} anos.")

# F strings são bem parecidad com o template string do Javascript 



# Métodos úteis de string:
frase = " Olá, mundo cruel! "

print("strip() -> remove espaços:", frase.strip())       # Remove espaços nas bordas
print("replace() -> troca palavras:", frase.replace("cruel", "lindo"))  # Substitui
print("split() -> separa por espaço:", frase.split())    # Separa palavras



# ------------------------------------
# 8. OPERADORES EM PYTHON
# ------------------------------------

# Aritméticos
a = 10
b = 3
print("Soma:", a + b)
print("Subtração:", a - b)
print("Multiplicação:", a * b)
print("Divisão real:", a / b)
print("Divisão inteira:", a // b)
print("Módulo (resto):", a % b)
print("Exponenciação:", a ** b)




# Comparação (retornam True ou False)
print("a == b:", a == b)   # Igual
print("a != b:", a != b)   # Diferente
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)




# Lógicos
x = True
y = False
print("x and y:", x and y)  # False
print("x or y:", x or y)    # True
print("not x:", not x)      # False




# Identidade
lista1 = [1, 2, 3]
lista2 = lista1
lista3 = [1, 2, 3]
print("lista1 is lista2:", lista1 is lista2)  # True (mesmo objeto na memória)
print("lista1 is lista3:", lista1 is lista3)  # False (objetos diferentes)
print("lista1 == lista3:", lista1 == lista3)  # True (valores iguais)




# Atribuição
numero = 5
numero += 2  # número = número + 2
print("Atribuição com +=:", numero)




# Operadores de Membro
frutas = ["maçã", "banana", "uva"]
print("'banana' in frutas:", "banana" in frutas)    # True
print("'pera' not in frutas:", "pera" not in frutas)  # True




# ------------------------------------
# 9. CONTROLE DE FLUXO EM PYTHON
# ------------------------------------

# if / elif / else
idade = 20
if idade < 18:
    print("Menor de idade")
elif idade == 18:
    print("Tem exatamente 18 anos")
else:
    print("Maior de idade")




# for loop
print("Contando de 1 a 5:")
for i in range(1, 6):
    print(i)




# while loop
contador = 0
print("Usando while para contar até 3:")
while contador < 3:
    print("Contador:", contador)
    contador += 1


    

# break e continue
print("Exemplo com break e continue:")
for i in range(5):
    if i == 2:
        continue  # pula o número 2
    if i == 4:
        break     # para o loop quando chega no 4
    print("Valor de i:", i)
