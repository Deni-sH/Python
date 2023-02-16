# def cria_matriz(tot_lin, tot_col, valor):
#     matriz = []  #lista vazia
#     for i in range(tot_lin):
#         linha = []
#         for j in range(tot_col):
#             linha.append(valor)
#         matriz.append(linha)
#     return matriz

# x = cria_matriz(1, 3, 99)



# A alternativa que representa a matriz que será armazenada em x se for digitado o seguinte comando: x = cria_matriz(1, 3, 99) é:

# [[99, 99, 99]]

# Isso ocorre porque a função cria uma matriz com uma única linha (tot_lin=1) e três colunas (tot_col=3), 
# em que cada elemento possui o valor 99 
# (valor=99). Portanto, a 
# matriz resultante tem uma única linha com três elementos, que são todos iguais a 99.def tarefa(mat):
def cria_matriz(num_linhas, num_colunas):
    matriz = []  #lista vazia
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            linha.append(0)
        matriz.append(linha)

    for i in range(num_colunas):
        for j in range(num_linhas):
            matriz[j][i] = int(input("Digite o elemento [" + str(j) + "][" + str(i) + "]: "))

    return matriz