import math

# Você também pode usar a função hypot que está presente no módulo math ou a função dist, que recebe duas sequências como 
# argumentos em sua chamada, sendo cada sequência os números que representam os valores X e Y de cada vetor, 
# nesse caso.import math

pontox1 = int(input("Digite um número: "))
pontoy1 = int(input("Digite um número: "))
pontox2 = int(input("Digite um número: "))
pontoy2 = int(input("Digite um número: "))

d_prov = math.sqrt((pontox1 - pontox2)**2) + math.sqrt((pontoy1 + pontoy2)**2)

if (d_prov >= 10):
    print("longe")
else:
    print("perto")
