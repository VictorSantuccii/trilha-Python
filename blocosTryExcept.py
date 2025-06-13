print("\n==== 1. Bloco try-except básico ====")

try:
    x = int(input("Digite um número inteiro: "))
    print("Você digitou:", x)
except:
    # Captura qualquer erro (geral, não recomendado no dia a dia)
    print("Erro: você não digitou um número inteiro.")

# -----------------------------------------

print("\n==== 2. try-except com exceções específicas ====")

try:
    a = int("abc")  # Vai causar ValueError
except ValueError:
    print("Erro: valor inválido, não é um número.")

# -----------------------------------------

print("\n==== 3. Múltiplos except ====")

try:
    lista = [1, 2, 3]
    print(lista[5])  # IndexError
except ValueError:
    print("Erro de valor.")
except IndexError:
    print("Erro: índice fora da lista.")
except Exception as e:
    print("Outro erro:", e)

# -----------------------------------------

print("\n==== 4. Bloco else ====")

# else só é executado se o try for bem-sucedido (sem erro)
try:
    num = int(input("Digite outro número: "))
except ValueError:
    print("Erro ao converter número.")
else:
    print("Conversão bem-sucedida! Dobro:", num * 2)

# -----------------------------------------

print("\n==== 5. Bloco finally ====")

# finally sempre executa, com ou sem erro
try:
    resultado = 10 / int(input("Digite um número para dividir 10: "))
except ZeroDivisionError:
    print("Erro: divisão por zero!")
except ValueError:
    print("Erro: digite um número válido.")
else:
    print("Resultado da divisão:", resultado)
finally:
    print("Fim do bloco try-except-finally.")  # Sempre será exibido

# -----------------------------------------

print("\n==== 6. Usando raise para lançar exceções personalizadas ====")

def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("Você tentou dividir por zero!")
    return a / b

try:
    print(dividir(10, 0))
except ZeroDivisionError as erro:
    print("Erro detectado:", erro)

# -----------------------------------------

print("\n==== 7. Criando sua própria exceção personalizada ====")

class IdadeInvalidaError(Exception):
    """Exceção personalizada para idade negativa"""
    pass

def verificar_idade(idade):
    if idade < 0:
        raise IdadeInvalidaError("Idade não pode ser negativa.")
    print(f"Idade registrada: {idade}")

try:
    verificar_idade(-5)
except IdadeInvalidaError as erro:
    print("Exceção personalizada capturada:", erro)

# -----------------------------------------

print("\n==== 8. Capturando a exceção como objeto ====")

try:
    int("xyz")
except ValueError as erro:
    print("Detalhes do erro:", erro)  # imprime a mensagem original do Python

# -----------------------------------------

print("\n==== 9. Try-except aninhado ====")

try:
    x = int(input("Digite um número: "))
    try:
        y = 10 / x
        print("Resultado:", y)
    except ZeroDivisionError:
        print("Erro interno: divisão por zero.")
except ValueError:
    print("Erro externo: número inválido.")

# -----------------------------------------

print("\n==== 10. Exemplo final: uso prático com arquivos ====")

try:
    caminho = "arquivo_inexistente.txt"
    with open(caminho, "r") as arquivo:
        conteudo = arquivo.read()
except FileNotFoundError:
    print(f"Erro: o arquivo '{caminho}' não foi encontrado.")
finally:
    print("Tentativa de leitura finalizada.")



# Bloco	O que faz
# try	Código que pode gerar erro
# except	Bloco que captura erro (pode ter mais de um)
# except as e	Captura o erro como objeto para inspecionar mensagem
# else	Executado se não ocorrer erro no try
# finally	Sempre executado, mesmo com erro
# raise	Lança uma exceção manualmente
# Exceções personalizadas	Criadas com classes herdando de Exception