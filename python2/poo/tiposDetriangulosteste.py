import pytest
from tiposDetriangulosEx2 import Triangulo

@pytest.mark.parametrize("ladoA, ladoB, ladoC, expected_output", [
    (1, 1, 1, "equilátero (todos os lados iguais)"),
    (1, 2, 2, "isósceles (dois lados iguais)"),
    (3, 4, 5, "escaleno (todos os lados diferentes)"),
    (1, 1, 2, "isósceles (dois lados iguais)"),
])
def test_tipo_lado(ladoA, ladoB, ladoC, expected_output):
    t = Triangulo(ladoA, ladoB, ladoC)
    assert t.tipo_lado() == expected_output
    
    
    
# Na função test_tipo_lado, estamos definindo quatro parâmetros:

# ladoA: o valor do primeiro lado do triângulo a ser testado.
# ladoB: o valor do segundo lado do triângulo a ser testado.
# ladoC: o valor do terceiro lado do triângulo a ser testado.
# expected_output: a saída esperada da função tipo_lado quando os valores dos lados são ladoA, ladoB e ladoC.
# Em seguida, estamos criando uma instância da classe Triangulo com os valores de ladoA, ladoB e ladoC, utilizando t = Triangulo(ladoA, ladoB, ladoC). 
# Isso cria um objeto Triangulo com os valores dos lados que queremos testar.

# Finalmente, estamos usando o assert para verificar se o resultado da função tipo_lado() para o objeto Triangulo criado com os valores de 
# ladoA, ladoB e ladoC é igual ao valor esperado de expected_output. Se o resultado for diferente do esperado, o teste falhará e o 
# pytest informará que algo deu errado. Se o resultado for igual ao esperado, o teste passará e o pytest seguirá para o próximo 
# conjunto de parâmetros definidos em @pytest.mark.parametrize.