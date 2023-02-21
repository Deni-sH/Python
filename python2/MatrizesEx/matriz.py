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
# def cria_matriz(num_linhas, num_colunas):
#     matriz = []  #lista vazia
#     for i in range(num_linhas):
#         linha = []
#         for j in range(num_colunas):
#             linha.append(0)
#         matriz.append(linha)

#     for i in range(num_colunas):
#         for j in range(num_linhas):
#             matriz[j][i] = int(input("Digite o elemento [" + str(j) + "][" + str(i) + "]: "))

#     return matriz

# Para executar a função minha_matriz que você criou, você precisa chamar a função em algum lugar do código e passar os argumentos corretos. Por exemplo, você pode adicionar o seguinte código no final do arquivo Python para criar uma matriz de 3 linhas por 4 colunas, com todos os elementos definidos como 0, e imprimir a matriz resultante no console:
# matriz = minha_matriz(3, 4, 0)
# print(matriz)
# Depois de adicionar esse código, você pode executar o arquivo Python no VS Code usando o recurso de execução integrado. Isso deve imprimir a matriz resultante no console.
# def minha_matriz(n_linhas, n_colunas, valor):
#     matriz = []
#     for i in range(n_linhas):
#         linha = []
#         for j in range(n_colunas):
#             linha.append(valor)
#         matriz.append(linha)
    
#     return matriz

# matriz = minha_matriz(3, 4, 0)
# print(matriz)
