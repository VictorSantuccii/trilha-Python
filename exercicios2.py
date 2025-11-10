# -----------------------------------------------
# Exercício 1: Ler 10 números e mostrar:
# a) A média dos números
# b) O maior e o menor número
# c) A lista completa
# -----------------------------------------------
lista = []
maiorNum = 0
menorNum = 0
somaNumeros = 0

for i in range(10):
    num = int(input("Digite números: "))

    somaNumeros += num
    
    if maiorNum == 0 or num > maiorNum:
        maiorNum = num
    if menorNum == 0 or num < menorNum:
        menorNum = num

    lista.append(num)

mediaNumeros = somaNumeros / 10

print(f"\nMédia dos números: {mediaNumeros}")
print(f"Lista completa: {lista}")
print(f"Maior número: {maiorNum}")
print(f"Menor número: {menorNum}")


# -----------------------------------------------
# Exercício 2: Ler idade e altura de 10 pessoas
# e mostrar na ordem inversa à leitura
# -----------------------------------------------
listaAltura = []
listaIdade = []

for i in range(10):
    idade = int(input("\nDigite sua idade: "))
    altura = float(input("Agora, digite sua altura: "))

    listaIdade.append(idade)
    listaAltura.append(altura)

print("\n--- Idades e alturas em ordem inversa ---")
for i in range(9, -1, -1):
    print(f"Pessoa {i+1}: idade = {listaIdade[i]}, altura = {listaAltura[i]}")


# -----------------------------------------------
# Exercício 3: Verificar se uma palavra, frase ou número
# é um palíndromo (mesma leitura da esquerda e direita)
# -----------------------------------------------
def eh_palindromo(texto):
    texto = texto.lower().replace(" ", "")  
    return texto == texto[::-1]  

palavra = input("\nDigite uma palavra, frase ou número: ")

if eh_palindromo(palavra):
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")


# -----------------------------------------------
# Exercício 4: Ler nome e idade de 30 pessoas e mostrar:
# a) Média das idades
# b) Quantos estão acima da média
# c) Nomes de quem está abaixo da média
# d) Pessoa mais velha e mais nova
# -----------------------------------------------
nomes = []
idades = []
i = 0
while i < 30:
    nome = input("\nDigite o nome da pessoa: ")
    idade = int(input("Digite a idade: "))
    if idade < 0 or nome == "":
        print("Valor inválido. Tente novamente.")
    else:
        nomes.append(nome)
        idades.append(idade)
        i += 1

soma = 0
for idade in idades:
    soma += idade
media = soma / 30

acima = 0
for idade in idades:
    if idade > media:
        acima += 1

abaixo_nomes = []
for i in range(30):
    if idades[i] < media:
        abaixo_nomes.append(nomes[i])

maior = idades[0]
menor = idades[0]
nome_maior = nomes[0]
nome_menor = nomes[0]

for i in range(1, 30):
    if idades[i] > maior:
        maior = idades[i]
        nome_maior = nomes[i]
    if idades[i] < menor:
        menor = idades[i]
        nome_menor = nomes[i]

print("\n--- Resultados ---")
print("Média das idades:", media)
print("Quantidade acima da média:", acima)
print("Pessoas abaixo da média:", abaixo_nomes)
print("Pessoa mais velha:", nome_maior, "-", maior, "anos")
print("Pessoa mais nova:", nome_menor, "-", menor, "anos")
