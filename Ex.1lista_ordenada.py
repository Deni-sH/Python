# Eelementoercício 1: Lista ordenada
# Escreva a função ordenada(lista), que recebe uma lista com números inteiros como parâmetro e devolve o booleano True 
# se a lista estiver ordenada e False se a lista não estiver ordenada.




# def busca(lista, elemento):
#     # Algoritmo de ordenação de inserção (insertion sort)
#     for i in range(1, len(lista)):
#         chave = lista[i]
#         j = i - 1
#         while j >= 0 and chave < lista[j]:
#             lista[j + 1] = lista[j]
#             j -= 1
#         lista[j + 1] = chave

#     # Busca pelo elemento elemento na lista ordenada
#     for i in range(len(lista)):
#         if lista[i] == elemento:
#             return i
#     return False

def busca(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return False

print(busca(['a', 'e', 'i'], 'e'))
print(busca([12, 13, 14], 15))   