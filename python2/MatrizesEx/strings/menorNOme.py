# Exercício 2: Menor nome
#escreva uma função menor_nome(nomes) que recebe uma lista de strings 
# com nome de pessoas como parâmetro e devolve o nome mais curto presente na lista.

# A função deve ignorar espaços antes e depois do nome= strip. e deve devolver o menor nome presente na lista =. Este nome 
# deve ser devolvido com a primeira letra maiúscula e seus demais caracteres minúsculos, independente de como 
# tenha sido apresentado na lista passada para a função.

# Quando houver mais de um nome com o menor comprimento dentre os nomes na lista, a função deve devolver o 
# primeiro nome com o menor comprimento presente na lista.

def menor_nome(nomes):
    menor_nome = nomes[0].strip() #No caso do código menor_nome = nomes[0].strip(), estamos definindo que menor_nome é igual ao primeiro nome da lista nomes
    menor_tamanho = len(menor_nome)
    
    for nome in nomes:
        nome = nome.strip()
        tamanho = len(nome)
        if tamanho < menor_tamanho:
            menor_tamanho = tamanho
            menor_nome = nome
            
    return menor_nome.capitalize() #letra maiuscula


print(menor_nome(['maria', 'josé', 'PAULO', 'Catarina'])) # 'José'
print(menor_nome(['maria', ' josé  ', '  PAULO', 'Catarina  '])) # 'José'
print(menor_nome(['Bárbara', 'JOSÉ  ', 'Bill'])) # 'José'