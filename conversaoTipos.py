# 🔄 Conversão de tipos em Python (type casting)




# ✅ int() → converte para inteiro

num_str: str = "10"
num_int: int = int(num_str)  # "10" → 10





# ✅ float() → converte para ponto flutuante

pi_str: str = "3.14"
pi_float: float = float(pi_str)  # "3.14" → 3.14





# ✅ str() → converte para string

idade: int = 25
idade_str: str = str(idade)  # 25 → "25"





# ✅ bool() → converte para booleano

# Regras:
# - False se for: "", 0, 0.0, None, [], (), {}, set()
# - True para todo o resto
texto: str = "Python"
flag: bool = bool(texto)  # "Python" → True





# ✅ list(), tuple(), set() → conversão entre coleções
valores: str = "abc"
lista: list = list(valores)   # "abc" → ['a', 'b', 'c']
tupla: tuple = tuple(valores) # "abc" → ('a', 'b', 'c')
conjunto: set = set(valores)  # "abc" → {'a', 'b', 'c'}





# ⚠️ Erros comuns:
# int("abc") → ValueError
# float("10,5") → ValueError (usa ponto, não vírgula)

# 📌 Dica: use try/except se a entrada pode dar erro