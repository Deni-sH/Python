
# Eelementoercício 1: Busca binária
# Implemente a função busca(lista, elemento), que busca um determinado elemento em uma lista e devolve o índice correspondente à posição do elemento encontrado. 
# Utilize o algoritmo de busca binária. Nos casos em que o elemento buscado não existir na lista, a função deve devolver o booleano False.

# Além de devolver o índice correspondente à posição do elemento encontrado, sua função deve imprimir cada um dos índices testados pelo algoritmo.

# def busca(lista, elemento):
#     primeiro = 0
#     ultimo = len(lista) - 1
#     encontrou = False
    
#     while primeiro <= ultimo:
#         meio = (primeiro + ultimo) // 2
#         print(meio)
#         if lista[meio] == elemento:
#             encontrou = True
#             return meio
#         elif lista[meio] > elemento:
#             ultimo = meio - 1
#         else:
#             primeiro = meio + 1
    
#     return encontrou


# lista = [-100, 0, 20, 30, 50, 100, 3000, 5000]

# busca(lista, 20)
# numerobinario = busca(lista, 100)
# print(numerobinario)


def busca(lista, elemento):
    primeiro = 0
    ultimo = len(lista) -1
    encontrou = False
    
    while primeiro <= ultimo:
        meio = (primeiro + ultimo) //2
        print(meio)
        
        if lista[meio] == elemento:
            encontrou = True
            return meio
        elif lista[meio] > elemento:
            primeiro =lista[meio] +1
        else:
            ultimo = lista[meio] -1
    return encontrou


# Quando estamos buscando um elemento em uma lista ordenada usando a busca binária, precisamos atualizar o intervalo de busca a cada iteração do laço. 
# Para fazer isso, usamos a posição do elemento central do intervalo atual, que é calculada como (primeiro + ultimo) // 2.

# Se o elemento central é maior que o elemento buscado, isso significa que o elemento buscado deve estar à esquerda do elemento central, 
# portanto atualizamos o valor de ultimo para a posição imediatamente anterior ao elemento central, ou seja, ultimo = meio - 1.

# Se o elemento central é menor que o elemento buscado, isso significa que o elemento buscado deve estar à direita do elemento central, 
# portanto atualizamos o valor de primeiro para a posição imediatamente posterior ao elemento central, ou seja, primeiro = meio + 1.

# Ao atualizarmos ultimo com lista[meio] + 1, estamos avançando o intervalo de busca para além do elemento central, o que pode fazer com que 
# percamos elementos relevantes para a busca.

# Por exemplo, se estivermos procurando o elemento 7 na lista [1, 3, 5, 7, 9, 11, 13] e o elemento central for 5, atualizar ultimo com lista[meio] + 1 
# fará com que o intervalo de busca avance para [9, 11, 13], perdendo assim o elemento 7 que está à esquerda do elemento central.