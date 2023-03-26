# def x(n):
#     if n >= 0 and n <= 2:
#         return n
#     else:
#         return x(n-1) + x(n-2) + x(n-3)

# print(x(6))





# O cálculo do número de chamadas recursivas é feito somando as chamadas de todas as chamadas recursivas que são feitas na execução do algoritmo.

# No caso desse algoritmo, para calcular o valor de x(6), o algoritmo precisa calcular o valor de x(5), x(4), e x(3), que por sua vez precisam calcular os valores
# anteriores x(4), x(3), x(2), x(2), x(1), x(0) e assim por diante até chegar nas chamadas iniciais de x(2), x(1) e x(0) que são retornadas imediatamente. 
# Cada chamada recursiva é contada separadamente, então o número total de chamadas é a soma de todas as chamadas que foram feitas.

# Para esse algoritmo em particular, o número de chamadas recursivas para calcular x(6) é 45.
#n = 6


#5 4 3 +6+6+6
# + 4 3 2 +  = 

# def x(n, cont=0):
#     cont += 1
#     if n >= 0 and n <= 2:
#         return n, cont
#     else:
#         res1, cont1 = x(n-1, cont)
#         res2, cont2 = x(n-2, cont)
#         res3, cont3 = x(n-3, cont)
#         return res1 + res2 + res3, cont1 + cont2 + cont3
    
# print(x(6))



# def busca_binaria(lista, elemento, min=0, max=None):
#     if max == None:
#         max = len(lista)-1

#     if max < min:
#         return False
#     else:
#         meio = min + (max-min)//2

#     if lista[meio] > elemento:
#         return busca_binaria(lista, elemento, min, meio - 1)
#     elif lista[meio] < elemento:
#         return busca_binaria(lista, elemento, meio + 1, max)
#     else:
#         return meio
    
    
    
#     a = [-10, -2, 0, 5, 66, 77, 99, 102, 239, 567, 875, 934]


# def x(n):
#     if n == 0:
#         print(n)
#     else:
#         x(n-1)
#         print(n) 
     
# print(x(10))
# r=
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10



# def x(n, m):
#     if n == m or m == 0:
#         return 1
#     else:
#         return x(n-1,m) + x(n-1,m+1)

# print(x(5,3))

# resultado = x(5,3)
# print(resultado)
def x(n, m):
    if n == m or m == 0:
        return 1
    else:
        return x(n-1,m) + x(n-1,m+1)

print(x(5,3))





def x(n):
    if n >= 0 and n <= 2:
        return n
    else:
        return x(n-1) + x(n-2) + x(n-3)

print(x(6))

# r = Resultado: 20. Chamadas recursivas: 24  