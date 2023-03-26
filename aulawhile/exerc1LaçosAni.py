# Exercício 1
# Escreva um programa que recebe como entradas (utilize a função input) dois números inteiros correspondentes à largura e à altura de um retângulo, 
# respectivamente. O programa deve imprimir, usando repetições encaixadas (laços aninhados), uma cadeia de caracteres que represente o retângulo informado 
# com caracteres '#' na saída.


# larg_ret = int(input("digite a largura: "))
# alt_ret = int(input("digite a altura: "))

# i = 0
# while i < alt_ret:
#     j = 0
#     while j < larg_ret:
#         print("#", end="")
#         j = j + 1
#     print()
#     i = i + 1

# largura = int(input("Digite a largura: "))
# altura = int(input("Digite a altura: "))

# for i in range(altura):
#     for j in range(largura):
#         print("#", end="")
#     print()  # Pula para a próxima linha


largura = int(input("digite a largura: ")) 
altura = int(input("digite a altura: "))

i = 0
while i < altura:
    j = 0
    while j < largura:
        print("#", end="")
        j = j + 1
    print()   
    i = i + 1