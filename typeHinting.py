# Importamos o módulo 'typing' para utilizar tipos mais complexos
from typing import List, Tuple, Dict, Optional, Union, Any

# Função com anotações de tipo simples
def saudacao(nome: str, idade: int) -> str:
    """
    Recebe um nome (str) e uma idade (int) e retorna uma saudação (str).
    """
    return f"Olá, {nome}! Você tem {idade} anos."


# Função que retorna uma lista de inteiros
def gerar_lista_de_numeros(qtd: int) -> List[int]:
    """
    Gera uma lista de números inteiros de 0 até qtd-1.
    """
    return list(range(qtd))


# Função que retorna uma tupla com nome e idade
def obter_usuario() -> Tuple[str, int]:
    """
    Retorna uma tupla contendo o nome (str) e idade (int) de um usuário.
    """
    return ("Ana", 30)


# Função que recebe um dicionário com nome (str) como chave e idade (int) como valor
def mostrar_idades(pessoas: Dict[str, int]) -> None:
    """
    Mostra o nome e idade de várias pessoas a partir de um dicionário.
    """
    for nome, idade in pessoas.items():
        print(f"{nome} tem {idade} anos")


# Função que recebe um valor que pode ser um int ou None
def dobrar(valor: Optional[int]) -> Optional[int]:
    """
    Dobra o valor se não for None. Caso seja None, retorna None.
    """
    if valor is None:
        return None
    return valor * 2


# Função que recebe valor que pode ser int ou str
def mostrar_valor(valor: Union[int, str]) -> str:
    """
    Mostra o valor recebido, que pode ser int ou str.
    """
    return f"Valor: {valor}"


# Função que recebe qualquer tipo de dado
def processar_dado(dado: Any) -> None:
    """
    Mostra qualquer dado recebido. Pode ser de qualquer tipo.
    """
    print(f"Dado recebido: {dado}")


# -----------------------------
# Exemplo de execução das funções

print(saudacao("Carlos", 25))  # str + int => retorna saudação
print(gerar_lista_de_numeros(5))  # List[int]
print(obter_usuario())  # Tuple[str, int]

mostrar_idades({"João": 22, "Maria": 28})  # Dict[str, int]

print(dobrar(10))     # Optional[int] → 20
print(dobrar(None))   # Optional[int] → None

print(mostrar_valor("dez"))  # Union[int, str]
print(mostrar_valor(10))

processar_dado(3.14)        # Any → float
processar_dado(["x", "y"])  # Any → list
