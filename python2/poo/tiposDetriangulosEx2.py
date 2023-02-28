# Exercício 2: Tipos de triângulos
# Na classe triângulo, definida na Questão 1, escreva o metodo tipo_lado() que devolve uma string dizendo se o triângulo é:

# isósceles (dois lados iguais)

# equilátero (todos os lados iguais)

# escaleno (todos os lados diferentes)

# Note que se o triângulo for equilátero, a função não deve devolver isóceles.

class Triangulo:
    def __init__(self, a, b, c):
        self.ladoA = a
        self.ladoB = b
        self.ladoC = c

    def perimetro(self):
        return self.ladoA + self.ladoB + self.ladoC


    def tipo_lado(self):
        if self.ladoA == self.ladoB and self.ladoB == self.ladoC:
            return ("equilátero")
        elif self.ladoA == self.ladoB or self.ladoA == self.ladoC or self.ladoB == self.ladoC:
            return ("isósceles")
        else:
            return ("escaleno")

t = Triangulo(1, 3, 5)
print("o triângulo é: ", t.tipo_lado())
