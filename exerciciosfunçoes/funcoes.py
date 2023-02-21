# def soma (x, y):
# 	return x + y
# print (soma(10, 20))
# print (soma(-20, 100))


# print(soma(20*32, soma(3, 4)))
# #20*32, soma(7)
# #640+7 =647


# Se você tivesse que resolver o seguinte exercício:

# "Desenvolva uma função que devolva um número lido, maior que zero",

# qual(is) das opções abaixo resolveria(m) seu problema? def leitura():
#     x = int(input("Digite um valor: "))
#     while x <= 0:
#         x = int(input("Digite um valor: "))
#     return x

# r: A função apresentada resolve o problema proposto pelo exercício, pois lê um valor digitado 
# pelo usuário usando a função input(), converte o valor para um número inteiro usando a função int(), 
# verifica se o valor é menor ou igual a zero, e se for, solicita ao usuário que digite outro valor. 
# O loop continua até que o usuário digite um valor maior que zero. Quando o valor digitado pelo usuário 
# for maior que zero, a função retorna o valor usando a declaração return.

# Assim, a função leitura() apresentada pode ser usada para resolver o problema proposto pelo exercício.


# Diferença entre print e return
# Neste ponto do curso, alguns alunos confundem a chamada da função print com o comando return. Os dois possuem propósitos bem diferentes:

# O print é uma função que serve apenas para imprimir valores na saída. O valor é mostrado ao usuário mas não  é enviado ao código que chamou aquela função. 

# Já o return, serve para encerrar a execução da função e devolver um valor (neste caso, muita gente usa a expressão "retornar um valor").

# Assim, quando um exercício pedir uma função que devolve um determinado valor, o comando return valor deve ser executado por essa 
# função (valor é a variável ou qualquer expressão com o valor a ser devolvido).


# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     continue
#   print(x)
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     continue
#   print(x)
#apple
# Result Size: 668 x 470
# for x in range(6):
#   print(x) 
# ​
# 0
# 1
# 2
# 3
# 4
# 5
# The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):
# for x in range(2, 30, 3):
#   print(x) 

# 2
# 5
# 8
# 11
# 14
# 17
# 20
# 23
# 26
# 29
# Else in For Loop
# The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
# for x in range(6):
#   print(x)
# else:
#   print("Finally finished!")

# 0
# 1
# 2
# 3
# 4
# 5
# Finally finished!

