#Escreva um programa que receba um número inteiro na entrada, calcule e imprima a soma dos dígitos deste número na saída

# n = input("Digite um número inteiro: ")

# print(sum(int(i) for i in n))




# def digitos(n):
#     n = abs(n)
#     while n > 0:
#         n, d = divmod(n, 10)
#         yield d

# n = int(input('Digite um número: '))
# soma = sum(digitos(n))


n = int(input("Digite um número inteiro: "))
if n > 0:
            soma = 0
            while n != 0:
                resto = n % 10
                n = (n - resto) // 10
                soma = soma + resto
            print(soma)
else: 
     print(n)
