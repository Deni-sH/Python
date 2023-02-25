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

# def calculo(x, y = 10, z = 5):
#     return x + y * z
# print(calculo(1, 2, 3))
# = 7


#----------------------------------------------------

# def horario_em_segundos(h, m, s):
#     assert h >= 0 and m >= 0 and s >= 0
#     return h * 3600 + m * 60 + s

# print(horario_em_segundos (10,-10,34))

#---------------------------------------------------------------------------------------------------

# Módulos são compostos por funções (definições) e podem ter outros comandos (statements)   ?
# Sim, módulos em Python podem ser compostos por funções e outros comandos (statements), como atribuições, condicionais, 
# loops, entre outros. Esses comandos e funções podem ser importados em outros módulos ou programas Python, permitindo 
# reutilização de código e modularidade. Além disso, é possível criar pacotes de módulos, que agrupam diversos módulos 
# relacionados em um mesmo diretório.


# Módulo podem se tornar uma entrada para o interpretador Python e assim ele é chamado de script?
# Sim, isso é correto. Um módulo Python pode ser executado como um script, fazendo com que o interpretador execute o código 
# contido nele. Para executar um módulo como um script, podemos usar o comando "python nome_do_modulo.py" no terminal.

# Módulos é o mesmo que funções  
# Não, módulos e funções são conceitos diferentes em Python.
# Módulos são arquivos que contêm definições de classes, funções e variáveis que podem ser utilizados em outros programas Python.
# Funções são blocos de código que realizam uma tarefa específica e podem ser chamadas e reutilizadas em diferentes partes do código.
# Embora módulos possam conter funções, eles não são a mesma coisa. Os módulos são uma forma de organizar e reutilizar o código, enquanto as 
# funções são blocos de código que executam tarefas específicas.

