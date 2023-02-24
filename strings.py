# '7 - 4'

# 22 // 5  . 2 barras nao era pra virar fracionado?
# Não, quando você usa a operação de divisão inteira // o resultado é sempre arredondado para baixo para o inteiro mais próximo. P
# # ortanto, o resultado de 22 // 5 é 4, que é a parte inteira da divisão de 22 por 5.


#  "15" + str(34)
# = '1534'  

# 'Python!' * 5
# ='Python!Python!Python!Python!Python!'

# palavra = "Python"

# palavra[3]
# =h
# -----------------------------------------------
# frase = " Python É Uma Linguagem Poderosa "
# frase.lower()
# = ' python é uma linguagem poderosa '

# frase = " Python É Uma Linguagem Poderosa "
# frase[:6]
# = Pytho


# frase = " Python É Uma Linguagem Poderosa "
# frase[14:]

# ='Linguagem Poderosa '


# frase = " Python É Uma Linguagem Poderosa "
# frase.replace("Poderosa", "Avançada")
# = ' Python É Uma Linguagem Avançada '

# frase = " Python É Uma Linguagem Poderosa "
# frase.strip()
# = 'Python É Uma Linguagem Poderosa'

# frase = " Python É Uma Linguagem Poderosa "
# frase.upper()

#-------------------------------------------------

# frase = "São Paulo é a maior cidade do Brasil"
# frase.count("o")
# 4

# frase = "São Paulo é a maior cidade do Brasil"
# frase.find("ai")

# frase = "São Paulo é a maior cidade do Brasil"
# len(frase)
#  36

# frase = "São Paulo é a maior cidade do Brasil"
# frase.find("w")

# achar a orden lexicográfica: >>> ord("a")   
# 97

# def fazAlgo(string):
#     pos = len(string)-1
#     string = string.upper()
#     while pos >= 0:
#         print(string[pos],end = "")
#         pos = pos - 1

# fazAlgo("paralelepipedo")

#= ODEPIPELELARAP>>> 

# A função fazAlgo(string) recebe uma string como argumento e a converte para letras maiúsculas usando o método upper(). Em seguida, 
# ela começa a imprimir cada caractere da string em ordem reversa, ou seja, do último para o primeiro. O loop que realiza essa tarefa 
# é controlado pela variável pos, que é inicializada com o valor do índice do último caractere da string (ou seja, len(string)-1). O loop 
# continua enquanto pos for maior ou igual a 0. O resultado de chamar a função fazAlgo("paralelepipedo") será a impressão da string "ODEPIPELELARAP" 
# na saída padrão (console). Note que a primeira letra "O" é a última letra da string original "paralelepipedo".

# def fazAlgo(string):
#     pos = 0
#     string1 = ""
#     string = string.lower()
#     stringMa = string.upper()
#     while pos < len(string):
#         if pos % 2 == 0:
#             string1 = string1 + stringMa[pos]
#         else:
#             string1 = string1 + string[pos]
#         pos = pos + 1
#     return string1    

# print(fazAlgo("paralelepipedo"))
#-------------------------------------------------------------------------------------------------
#Capitaliza letras alternadas  -  PaRaLeLePiPeDo  
# def fazAlgo(string):
#    pos = 0
#    string1 = ""
#    while pos < len(string):
#          if string[pos] != " ":
#              string1 = string1 + string[pos]
#          pos = pos + 1
#    return string1

# print(fazAlgo("É UM TESTE"))
# = ÉUMTESTE


#OR


# def fazAlgo(string):
#    pos = 0
#    string = string.lower()
#    string1 = ""
#    while pos < len(string):
#          if string[pos] != " ":
#              string1 = string1 + string[pos]
#          pos = pos + 1
#    return string1

# print(fazAlgo("É UM TESTE"))
# = éumteste


#-------------------------------------------------------------------------------------------------


# def fazAlgo(string):
#     pos = 0
#     string1 = ""
#     while pos < len(string):
#         if string[pos] != " ":
#             string1 = string1 + string[pos]
#         pos = pos + 1
#         string1 = string1.capitalize()  
#     return string1    

# print(fazAlgo("É UM TESTE"))

# =Éumteste