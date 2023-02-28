# Exercício 1: Uma classe para triângulos
# Defina a classe Triangulo cujo construtor recebe 3 valores inteiros correspondentes aos lados a, b e c de um triângulo.

# A classe triângulo também deve possuir um método perimetro, que não recebe parâmetros e devolve um valor inteiro correspondente ao perímetro do triângulo.



        
class Triangulo:
    def __init__(self, a, b, c):
        self.ladoA = a
        self.ladoB = b
        self.ladoC = c

    def perimetro(self):
        return self.ladoA + self.ladoB + self.ladoC


t = Triangulo(1, 1, 1)
print("Perímetro do triângulo:", t.perimetro())