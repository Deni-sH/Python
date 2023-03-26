# Exercício 1: Soma dos elementos de uma lista
# Implemente a função soma_lista(lista), que recebe como parâmetro uma lista de números inteiros e devolve um número inteiro correspondente 
# à soma dos elementos desta lista.

def soma_lista(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return lista[0] + soma_lista(lista[1:])
    
    
    
# lista = [1, 2, 3, 4, 5]

# resultado = soma_lista(lista)
# print(resultado)



# A primeira chamada da função recebe a lista [1, 2, 3, 4, 5]. Como a lista tem mais de um elemento, a função entra na condição else e retorna o 
# resultado da soma do primeiro elemento da lista (1) com o resultado da chamada recursiva da função soma_lista passando como argumento a fatia da 
# lista que começa no segundo elemento ([2, 3, 4, 5]).
# Na segunda chamada, a função recebe a lista [2, 3, 4, 5]. Novamente, a lista tem mais de um elemento, então a função entra no else e retorna a 
# soma do primeiro elemento da lista (2) com o resultado da chamada recursiva da função soma_lista passando como argumento a fatia da lista que começa no segundo elemento ([3, 4, 5]).
# Este processo continua até que a lista tenha apenas um elemento, quando a função retorna o próprio elemento.
# Então, o resultado final é a soma de todos os elementos da lista: 1 + 2 + 3 + 4 + 5 = 15.