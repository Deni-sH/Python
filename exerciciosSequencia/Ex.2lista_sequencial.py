
# Exercício 2: Busca sequencial
# Implemente a função busca(lista, elemento), que busca um determinado elemento em uma lista e devolve o índice correspondente à posição do elemento encontrado.
# Utilize o algoritmo de busca sequencial. Nos casos em que o elemento buscado não existir na lista, a função deve devolver o booleano False.


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