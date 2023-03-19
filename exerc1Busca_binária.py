
# Eelementoercício 1: Busca binária
# Implemente a função busca(lista, elemento), que busca um determinado elemento em uma lista e devolve o índice correspondente à posição do elemento encontrado. 
# Utilize o algoritmo de busca binária. Nos casos em que o elemento buscado não existir na lista, a função deve devolver o booleano False.

# Além de devolver o índice correspondente à posição do elemento encontrado, sua função deve imprimir cada um dos índices testados pelo algoritmo.

def busca(lista, elemento):
    primeiro = 0
    ultimo = len(lista) - 1
    encontrou = False
    
    while primeiro <= ultimo:
        meio = (primeiro + ultimo) // 2
        print(meio)
        if lista[meio] == elemento:
            encontrou = True
            return meio
        elif lista[meio] > elemento:
            ultimo = meio - 1
        else:
            primeiro = meio + 1
    
    return encontrou


# lista = [-100, 0, 20, 30, 50, 100, 3000, 5000]

# busca(lista, 20)
# numerobinario = busca(lista, 100)
# print(numerobinario)