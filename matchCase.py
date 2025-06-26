# Exercício 1
dia = int(input("1. Digite um número de 1 a 7: "))
match dia:
    case 1: print("Domingo")
    case 2: print("Segunda-feira")
    case 3: print("Terça-feira")
    case 4: print("Quarta-feira")
    case 5: print("Quinta-feira")
    case 6: print("Sexta-feira")
    case 7: print("Sábado")
    case _: print("Número inválido!")

# Exercício 2
mes = int(input("2. Digite um número de 1 a 12: "))
match mes:
    case 1: print("Janeiro")
    case 2: print("Fevereiro")
    case 3: print("Março")
    case 4: print("Abril")
    case 5: print("Maio")
    case 6: print("Junho")
    case 7: print("Julho")
    case 8: print("Agosto")
    case 9: print("Setembro")
    case 10: print("Outubro")
    case 11: print("Novembro")
    case 12: print("Dezembro")
    case _: print("Número inválido!")

# Exercício 3
letra = input("3. Digite uma letra (A, B, C ou D): ").upper()
match letra:
    case "A": print("Você escolheu A: Excelente!")
    case "B": print("Você escolheu B: Muito bom!")
    case "C": print("Você escolheu C: Bom!")
    case "D": print("Você escolheu D: Pode melhorar.")
    case _: print("Letra inválida!")

# Exercício 4
continente = int(input("4. Digite um número de 1 a 6 (continente): "))
match continente:
    case 1: print("África")
    case 2: print("América")
    case 3: print("Antártida")
    case 4: print("Ásia")
    case 5: print("Europa")
    case 6: print("Oceania")
    case _: print("Número inválido!")

# Exercício 5
cor = int(input("5. Digite um número de 1 a 5: "))
match cor:
    case 1: print("Vermelho")
    case 2: print("Azul")
    case 3: print("Verde")
    case 4: print("Amarelo")
    case 5: print("Roxo")
    case _: print("Número inválido!")

# Exercício 6
conceito = input("6. Digite uma nota de conceito (A, B, C, D, F): ").upper()
match conceito:
    case "A": print("Excelente desempenho!")
    case "B": print("Bom trabalho!")
    case "C": print("Você passou.")
    case "D": print("Atenção! Pode melhorar.")
    case "F": print("Reprovado.")
    case _: print("Conceito inválido!")

# Exercício 7
numero = int(input("7. Digite um número de 0 a 9: "))
match numero:
    case 0: print("Zero")
    case 1: print("Um")
    case 2: print("Dois")
    case 3: print("Três")
    case 4: print("Quatro")
    case 5: print("Cinco")
    case 6: print("Seis")
    case 7: print("Sete")
    case 8: print("Oito")
    case 9: print("Nove")
    case _: print("Número inválido!")

# Exercício 8
operacao = int(input("8. Escolha a operação (1-somar, 2-subtrair, 3-multiplicar, 4-dividir): "))
match operacao:
    case 1: print("Você escolheu somar.")
    case 2: print("Você escolheu subtrair.")
    case 3: print("Você escolheu multiplicar.")
    case 4: print("Você escolheu dividir.")
    case _: print("Opção inválida!")

# Exercício 9
animal = input("9. Digite o nome de um animal (ex: gato, cachorro, vaca): ").lower()
match animal:
    case "gato": print("O gato faz: Miau!")
    case "cachorro": print("O cachorro faz: Au au!")
    case "vaca": print("A vaca faz: Muuu!")
    case _: print("Animal desconhecido!")

# Exercício 10
fruta = input("10. Escolha uma fruta (banana, maçã, morango): ").lower()
match fruta:
    case "banana": print("Banana é rica em potássio!")
    case "maçã": print("Maçã ajuda na digestão.")
    case "morango": print("Morango é cheio de antioxidantes.")
    case _: print("Fruta inválida!")

# Exercício 11
estacao = int(input("11. Digite um número de 1 a 4 para a estação do ano: "))
match estacao:
    case 1: print("Primavera")
    case 2: print("Verão")
    case 3: print("Outono")
    case 4: print("Inverno")
    case _: print("Número inválido!")

# Exercício 12
turno = input("12. Digite seu turno (M - manhã, T - tarde, N - noite): ").upper()
match turno:
    case "M": print("Bom dia!")
    case "T": print("Boa tarde!")
    case "N": print("Boa noite!")
    case _: print("Turno inválido!")

# Exercício 13
direcao = input("13. Digite uma direção (Norte, Sul, Leste, Oeste): ").capitalize()
match direcao:
    case "Norte": print("O Norte é conhecido por suas paisagens geladas.")
    case "Sul": print("O Sul tem belas tradições culturais.")
    case "Leste": print("O Leste vê o nascer do sol primeiro.")
    case "Oeste": print("O Oeste tem belos pôr do sol.")
    case _: print("Direção inválida!")

# Exercício 14
personagem = input("14. Escolha um personagem (mago, guerreiro, arqueiro): ").lower()
match personagem:
    case "mago": print("O mago controla poderosos feitiços.")
    case "guerreiro": print("O guerreiro é forte e resistente.")
    case "arqueiro": print("O arqueiro é ágil e preciso.")
    case _: print("Personagem inválido!")

# Exercício 15
num_ext = int(input("15. Digite um número de 1 a 3: "))
match num_ext:
    case 1: print("Um - Urso")
    case 2: print("Dois - Dromedário")
    case 3: print("Três - Tigre")
    case _: print("Número inválido!")
