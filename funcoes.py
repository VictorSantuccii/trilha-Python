def saudacao_pessoal(nome):
    print(f"Olá, {nome}!")

saudacao_pessoal("Sant")


# def nome_da_funcao(parametros_opcionais):
    # bloco de código
   # return resultado_opcional

# Essa é a formatação de uma função em Python 

print("\n==== 1. Função tradicional com parâmetros e retorno ====")

def saudacao(nome):
    return f"Olá, {nome}!"

print(saudacao("Sant"))



print("\n==== 2. Função sem parâmetros ====")

def ola_mundo():
    print("Olá, mundo!")

ola_mundo()



print("\n==== 3. Função com valor padrão (default value) ====")

def boas_vindas(nome="Visitante"):
    print(f"Bem-vindo, {nome}!")

boas_vindas()
boas_vindas("Bibizinha")



print("\n==== 4. Função com múltiplos argumentos ====")

def somar(a, b, c):
    return a + b + c

print(somar(1, 2, 3))



print("\n==== 5. Função com número variável de argumentos (*args) ====")

def somar_tudo(*args):
    # *args vira uma tupla
    print("Argumentos recebidos:", args)
    return sum(args)

print(somar_tudo(10, 20, 30))



print("\n==== 6. Função com argumentos nomeados (**kwargs) ====")

def imprimir_dados(**kwargs):
    # **kwargs vira um dicionário
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

imprimir_dados(nome="Sant", idade=25, curso="ADS")



print("\n==== 7. Função lambda ====")

# Função tradicional
def quadrado(x):
    return x * x


# Mesma função com lambda
quadrado_lambda = lambda x: x * x

print("Tradicional:", quadrado(4))
print("Lambda:", quadrado_lambda(4))



print("\n==== 8. Lambda em funções integradas ====")


nomes = ["ana", "Carlos", "beatriz", "Davi"]
# Ordenar ignorando maiúsculas e minúsculas
ordenado = sorted(nomes, key=lambda nome: nome.lower())
print("Nomes ordenados:", ordenado)

# Dobrar números com map
numeros = [1, 2, 3, 4]
dobrados = list(map(lambda x: x * 2, numeros))
print("Dobro:", dobrados)



print("\n==== 9. Função aninhada (nested) ====")

def funcao_mae():
    def funcao_filha():
        return "Sou a filha!"
    return funcao_filha()

print(funcao_mae())



print("\n==== 10. Função como parâmetro ====")

def aplicar(funcao, valor):
    return funcao(valor)

def triplo(x):
    return x * 3

print("Triplo:", aplicar(triplo, 5))



print("\n==== 11. Função que retorna outra função ====")

def multiplicador(fator):
    def multiplica(x):
        return x * fator
    return multiplica

dobrar = multiplicador(2)
triplicar = multiplicador(3)

print("Dobrar:", dobrar(10))
print("Triplicar:", triplicar(10))



print("\n==== 12. Função recursiva ====")

def fatorial(n):
    if n == 0:
        return 1
    return n * fatorial(n - 1)

print("Fatorial de 5:", fatorial(5))



print("\n==== 13. Função com anotação de tipo ====")

def somar_com_tipos(a: int, b: int) -> int:
    return a + b

print("Com anotação:", somar_com_tipos(10, 20))


#| Tipo de Função           | O que faz                                         | 
#| ------------------------ | ------------------------------------------------- |
#| `def`                    | Define uma função tradicional                     |
#| Sem parâmetros           | Executa algo sem entradas                         |
#| Com parâmetros           | Recebe valores na chamada                         |
#| Com valor padrão         | Usa um valor se nada for passado                  |
#| `*args`                  | Aceita número variável de argumentos (como tupla) |
#| `**kwargs`               | Aceita pares nome=valor (como dicionário)         |
#| `lambda`                 | Função anônima rápida de uma linha                |
#| Aninhada                 | Função dentro de função                           |
#| Como parâmetro           | Passa função como argumento                       |
#| Que retorna outra função | Retorna uma função (closure)                      |
#| Recursiva                | Chama a si mesma                                  |
#| Com anotação de tipo     | Ajuda na legibilidade e em IDEs                   |
