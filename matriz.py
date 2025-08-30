# Passo 1: Pedir ao usuário o tamanho da matriz
linhas = int(input("Digite o número de LINHAS da matriz: "))
colunas = int(input("Digite o número de COLUNAS da matriz: "))


# Passo 2: Criar uma matriz vazia
matriz = []


print("\nAgora digite os ELEMENTOS da matriz:")


# Passo 3: Preencher a matriz com valores informados pelo usuário
for i in range(linhas):
    linha = []  # cria uma linha temporária
    for j in range(colunas):
        valor = int(input(f"Digite o valor para a posição [{i}][{j}]: "))
        linha.append(valor)  # adiciona o valor na linha
    matriz.append(linha)  # adiciona a linha completa na matriz



# Passo 4: Exibir a matriz de forma organizada
print("\n📋 Matriz digitada:")
for linha in matriz:
    print(linha)



# Passo 5: Calcular a soma de todos os elementos da matriz
soma_total = 0
for i in range(linhas):
    for j in range(colunas):
        soma_total += matriz[i][j]



print(f"\n🔢 Soma de TODOS os elementos da matriz: {soma_total}")



# Passo 6: Verificar se a matriz é quadrada
if linhas == colunas:
    # Diagonal principal: elementos [0][0], [1][1], [2][2], ...
    soma_diagonal_principal = 0
    for i in range(linhas):
        soma_diagonal_principal += matriz[i][i]



    print(f"🔷 Soma da DIAGONAL PRINCIPAL: {soma_diagonal_principal}")



    # Diagonal secundária: elementos [0][n-1], [1][n-2], [2][n-3], ...
    soma_diagonal_secundaria = 0
    for i in range(linhas):
        soma_diagonal_secundaria += matriz[i][colunas - 1 - i]



    print(f"🔶 Soma da DIAGONAL SECUNDÁRIA: {soma_diagonal_secundaria}")
else:
    print("⚠️ A matriz não é quadrada, então não possui diagonais definidas.")
