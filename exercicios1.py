# Olá, mundo!
# Crie um programa que exiba “Olá, Mundo!” na tela.

print("Olá, Mundo!")

# Soma de números
#Peça dois números ao usuário e mostre a soma.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

soma = num1 + num2
print(f"A soma dos números é {soma}")

#Par ou ímpar
#Peça um número e diga se ele é par ou ímpar.

num1 = int(input("Digite um número: "))

if num1 % 2 == 0:
    print("Seu número é par")
else:
    print("Seu número é ímpar")



#Maior número
#Leia três números e mostre qual é o maior.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

if num1 > num2 and num1 > num3:
    print("O número 1 é maior")
elif num2 > num1 and num2 > num3:
    print("O número 2 é maior")
else:
    print("O número 3 é maior")


#Tabuada
#Mostre a tabuada de um número digitado pelo usuário (de 1 a 10).

print(" ----- Tabuada ----- \n")
num = int(input("Digite um número qualquer: "))

for i in range(11):
    print(f"A tabuada de {i} * {num} é: ", i * num)


#Contador
#Mostre todos os números de 1 a 100 com um loop for.

print(" ----- Loop 1 ao 100 ----- ")
for i in range(101):
    print("Contando de 1 ao 100: ", i )


#Conversor de temperatura
#Converta graus Celsius para Fahrenheit.

print( "----- Conversor de temperaturas ----- ")

celsius = int(input("Digite a temperatura atual em graus Celsius: "))

fahrenheit = (celsius * 1,8) + 32

print(f"A temperatura de Celsius em Fahrenheit é: {fahrenheit} ")

#Verificador de ano bissexto
#Receba um ano e diga se ele é bissexto.

print(" ----- Verificador de anos bissextos ----- ")

ano = int(input("Digite um ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"{ano} é um ano bissexto!")
else:
    print(f"{ano} não é bissexto.")



#Média escolar
#Peça 4 notas e mostre a média, indicando se o aluno foi aprovado (média ≥ 6).

print(" ----- Notas -----")

somaNotas = 0

for i in range(4):

    notas = int(input("Digite sua nota: "))

    somaNotas = somaNotas + notas
    print(somaNotas)


mediaNotas = somaNotas / 4

print("A média final das suas notas foi: ", mediaNotas)


#Número primo
#Verifique se um número é primo. 

print(" ----- Número primo ----- ")

numero = int(input("Digite um número: "))

if numero <= 1:
    print("Não é primo.")
else:
    for i in range(2, numero):
        if numero % i == 0:
            print("Não é primo.")
            break
    else:
        print("É primo!")
