# OVER: executa uma linha inteira e se nela tiver uma chamada de função, ela é executada por completo, de uma só vez, sem mostrar o passo a passo dentro dela (CORRETO)
# STEP: executa uma linha inteira e se nela tiver uma chamada de função, ele entra na função e executa passo a passo (CORRETO)
# Go: executa o programa inteiro (CORRETO)


def soma(num1, num2, num3):
    return num1 + num2 + num3

def main():
    n1 = float(input("Primeiro número = "))
    n2 = float(input("Segundo número = "))
    n3 = float(input("Terceiro número = "))
    print (soma(n1, n2, n3))

main()