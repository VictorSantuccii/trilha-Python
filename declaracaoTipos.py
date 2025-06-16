class Pessoa:
    nome: str
    idade: int
    ativo: bool

    def __init__(self, nome: str, idade: int, ativo: bool) -> None:
        self.nome = nome
        self.idade = idade
        self.ativo = ativo


class Produto:
    def __init__(self, nome: str, preco: float) -> None:
        self.nome: str = nome
        self.preco: float = preco



# from dataclasses import dataclass

@dataclass
class Livro:
    titulo: str
    autor: str
    paginas: int
    disponivel: bool = True  # Pode ter valores padrão


   # Com @dataclass, você não precisa escrever o __init__. Ele é gerado automaticamente com base nos tipos declarados.

   # Muito útil para classes que armazenam dados (sem muita lógica interna).
