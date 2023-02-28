
# similaridades com c 
# soma=5.5
# print("soma=",soma)

# o que é ciência da computação

# nova ciencia, engloba várias áreas do conhecimento humano
# matemática :diferentes aspectos computacionais

# engenharia: contruir sistemas computacionais complexos, software, hardware
# ciencias naturais: desenvolveram uma metodologia cientificas, hipoteses, teorias prever novos comportamentos/ experimentos
# arte: aspectos criativos, estética novas ideais codificadas na forma de software
# esporte: praticar bastante, manter resiliência para se manter fluente na linguagem.

# habiliaddes: capacidade de resolver problemas do mundo real computacionalmente.
# Formular um problema do mundo real em termos computacionais

# Elaborar uma solução para esse problema em termos computacionais.
# *algoritmo

# Escrever um programa em uma linguagem de programação que implemente esse algoritmo
# Testar o programa para verificar se ele realmente resolve esse problema

# habilidades mais avançadas.

# >Software de grande porte composto por muitos programas
# >Grandes quantidades de dados
# >Gerenciar equipes de desenvolvimento de software

# Comunicar-se com clientes e usuarios para entender seus problemas, dificuldades e necessidades


# Pergunta 5
# compilador é responsável por traduzir programas escritos em linguagem de alto nível para linguagem de máquina.

# Pergunta 2
# Software e programas(hardware não é) são instruções para o computador. (escolha todas as opções corretas)


# 22%3

# # len = lenght

# ordem = parêntesis>exponenciação>divisao e multi> adição e sub
# divisão em pythom = // e numero fload(fracionado) = /

# temperaturaFahrenheit = input("Digite uma temperatura em Fahrenheit")

# temp = int(temperaturaFahrenheit)
#como deu esse erro:     temperaduraCelsius = 5*((temperaturaFahrenheit - 32)/9)    
# TypeError: unsupported operand type(s) for -: 'str' and 'int'  = função input sempre devolve uma string e no caso ele devolve em uma conta numérica, então é necessário
                                                                    # converter para um inteiro/float
#                                                                   foi utilizado o float para transformar em número fracionario a variável fahrenheit
# temperaduraCelsius = 5*((temp-32)/9)

# print ("A temperatura é", temperaduraCelsius)

# = Digite uma temperatura em Fahrenheit78
# A temperatura é 25.555555555555554

# ou
# temperaturaFahrenheit = input("Digite uma temperatura em Fahrenheit")
# temperaduraCelsius = 5*((float(temperaturaFahrenheit)-32)/9)

# print ("A temperatura é", temperaduraCelsius)

# nomeDaMae = input("Qual o nome da sua mãe?")

# nomeDoPai = input("Qual o nome do seu pai?")

# print("Bom dia Srta.", nomeDaMae, "E bom dia Sr.", nomeDoPai.)


# segundos_str = input("Por favor, entre com o número de segundos que deseja converter: ")
# total_segs = int(segundos_str)

# horas = total_segs //3600
# segs_restantes = total_segs % 3600
# minutos = segs_restantes //60
# segs_restantes_final = segs_restantes % 60
# print(horas, "horas, ", minutos, "minutos e", segs_restantes_final, "segundos.")

# = Por favor, entre com o número de segundos que deseja converter: 7854
# 2 horas,  10 minutos e 54 segundos.
# PS C:\project\python_0.0> 
# x = input ("Qual a sua idade?")

# print(x)

# print ("olá" 'mundo') = olámundo
# --------------------------------------------------- EXERCICIOS
# a = int(input("Qual o valor de a? "))
# b = int(input("Qual o valor de b? "))
# a = b
# b = a
# print(a)
# print(b)
# r:Qual o valor de a? 1
# Qual o valor de b? 2
# 2
# 2


# Pergunta 3
# Quais os valores finais das variáveis a e b, se o usuário digitar 1 e 2, respectivamente?

# a = int(input("Qual o valor de a? "))
# b = int(input("Qual o valor de b? "))
# aux = a
# a = b
# b = aux
# print(a)
# print(b)


# 1.
# Pergunta 1
# Qual o tipo de dado armazenado na variável x pelo comando abaixo?
# R: 
# 
# a função input sempre devolve um string
# -------------------------------------------
# x = 10
# y = 15
# z = 25
# print(x == z - y and z != y - x or not y != z - x)

# true

# 8.
# Pergunta 8
# Considere x = 10, y = 20 e z = 30, assinale quais das alternativas  abaixo resultam em True:
    
#     print(not y < 10 or not z == 10) 

# Correto

# print(x >= 10 or y != z - x)

# Correto

# print(x <= 30 and y >= 5)

# Correto

# print(not y > 10 or not z > 10)

# Não deve ser selecionado

# tempoDeJogo = int(input("Quanto de tempo já jogamos?"))

# if tempoDeJogo <=90:
#         print("Ainda tem jogo pela frente")
#         print("que maravilia")
# else:
#         print("esta no fim do jogo")
#         print("Pode apitar juiz")
# 2.
# Pergunta 2
# Considere que a variável is_ready é do tipo booleano. Qual declaração está correta e é a forma mais sucinta de testar se is_ready é verdadeiro?

# 0 / 1 ponto

# if (is_ready  == True):


# if (is_ready): <----correta


# if (not is_ready  = False):


# if (is_ready  = True):


# if (not is_ready  == False):

# A função pode receber ou não parâmetros. Isso depende da tarefa que a função irá executar e da necessidade de receber dados de entrada para realizar essa tarefa.

# Em código bem feito, o nome da função deve representar a tarefa que ela irá executar. Isso ajuda a tornar o código mais legível e fácil de entender, pois indica claramente 
# qual é a finalidade da função.

# return é usado para a função devolver um determinado valor para quem a chamou. Isso é útil quando a função precisa retornar um resultado para o código que a chamou.

# A função pode ou não devolver valor. Algumas funções podem ser usadas apenas para realizar uma tarefa específica e não precisam retornar nenhum valor. Outras funções 
# podem ser usadas para realizar um cálculo ou uma operação e retornar um valor como resultado.

# Parâmetros de uma função são valores que ela recebe para trabalhar. Esses valores podem ser usados pela função para realizar uma tarefa específica ou para 
# influenciar o comportamento da função.



class Lista:
  def append(self, elemento):
    return "Oops! Este objeto não é uma lista"
    
lista = []

a = Lista()
b = a.append(7)

lista.append(b)
