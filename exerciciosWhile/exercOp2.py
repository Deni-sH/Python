#Escreva um programa que receba um número inteiro na entrada e 
# verifique se o número recebido possui ao menos um dígito com um 
# dígito adjacente igual a ele. Caso exista, imprima "sim"; se não existir, imprima "não".


# n = int(input("digite um numero: "))

# n1 = n

# rest1 = n % 10

# while (n // 10 != 0):

#        n = n // 10

#        rest = n % 10

#        if rest == rest1:

#                print("sim")

#                n = n1

#                break

#        rest1 = rest

# if n // 10 == 0:

#        print("nao")



n = int(input("Digite um número: "))
cond = True

while cond:
     dividido = n // 10
     resto = n % 10
     resto1 = dividido % 10
     
     if n <= 10:
         print("não")
         cond = False
         
     elif n > 10 and resto == resto1:
         print("sim")
         cond = False
     else:
         n = n//10