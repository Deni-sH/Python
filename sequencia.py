# Question 1
# Assinale a afirmação CORRETA:


# Busca sequencial é um algoritmo muito sofisticado que ordenada os dados de uma determinada lista

# A busca sequencial não é um algoritmo de ordenação de dados, mas sim um algoritmo de busca. 
# A busca sequencial percorre uma lista de dados de forma sequencial, comparando cada elemento 
# com o valor buscado até encontrar uma correspondência ou chegar ao final da lista.


# Busca sequencial é o algoritmo mais simples usado para encontrar um determinada dado dentro de uma lista

# Sim, você está correto. A busca sequencial é um dos algoritmos mais simples e básicos para buscar um determinado elemento dentro de uma lista. 
# Esse algoritmo percorre a lista elemento por elemento, comparando cada elemento com o valor buscado até encontrar o elemento desejado ou 
# chegar ao final da lista. Embora seja simples, a busca sequencial pode ser útil em algumas situações em que a lista não é muito grande 
# ou em que não é possível ordenar a lista de forma eficiente.


# 2.
# Question 2
# O que precisa ser mudado na função abaixo para que ela retorne a posição onde o elemento se encontra dentro da lista e -1 caso ele não exista.

# def busca_sequencial(seq, x):
#     for i in range(len(seq)):
#         if seq[i] == x:
#             return i
#     return -1

# lista = [3, 7, 1, 1, 5, 2]

# # Buscando o elemento 5 na lista
# posicao = busca_sequencial(lista, 5)

# # Imprimindo a posição do elemento na lista
# print(posicao)

# Nesse exemplo, a função busca_sequencial é chamada passando a lista [3, 7, 1, 5, 9, 2] e o valor 5 como argumentos. 
# A função retorna a posição do elemento na lista, que nesse caso é 3, pois o elemento 5 está na quarta posição da 
# lista (lembrando que a contagem começa em zero). Em seguida, a posição é impressa na tela usando a função print.

# Você pode modificar os valores da lista e do elemento buscado para testar diferentes casos de uso da função.



# Não, a função não vai rodar novamente em -1. Quando a função chegar ao comando "return -1", significa que o laço for terminou de 
# executar sem encontrar o elemento buscado na lista. Nesse caso, a função vai retornar imediatamente o valor -1 e não vai executar 
# mais nenhuma instrução dentro da função.

# O que acontece é que o laço for percorre toda a lista, verificando se cada elemento é igual ao valor buscado. Se o elemento for 
# encontrado na lista, a função vai retornar imediatamente o índice desse elemento. Se o laço terminar de executar sem encontrar o 
# elemento, a função vai retornar o valor -1.

# Portanto, a função busca_sequencial percorre a lista apenas uma vez e retorna imediatamente assim que encontra o elemento buscado 
# ou quando termina de percorrer a lista.



# 2----------------------------------------------

# def busca_sequencial(seq, x):
#     for i in range(len(seq)):
#         if seq[i] == x:
#             return True
#     return False

# numeros = [55,33,0,900,-432,123,77,10,11]

# posi = busca_sequencial(numeros, 55)

# print(posi)


# Question 5
# Analise o algoritmo de ordenação Seleção Direta abaixo e considere a lista numeros abaixo.

def selecao_direta(lista):
    fim = len(lista)
    for i in range(fim-1):
        pos_menor = i
        for j in range(i+1,fim):
            if lista[j] < lista[pos_menor]:
                pos_menor = j
        lista[i],lista[pos_menor] = lista[pos_menor],lista[i]
    return lista

numeros = [55,33,0,900,-432,10,77,123,11]

# Quantas vezes o valor 2 será trocado de lugar, dentro da lista, até ser colocado na posição certa da lista ordenada?

