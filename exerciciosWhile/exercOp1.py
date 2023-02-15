n = int(input("Digite um número"))
divisores = 0
for divisor in range(1, n):
    if n % divisor == 0:
        divisores = divisores + 1
        if divisores > 1:
          break
if (divisores > 1) or (divisores == 0):
  print("não primo")
else:
  print("é primo")