def fatorial(n):
    if n < 1:
        return 1
    else:
        return n * fatorial(n-1)
    
import pytest

@pytest.mark.parametrize("entrada, esperado", [
        (0,1),
        (1,1),
        (2,2),
        (3,6),
        (4,24),
        (5,10),
        (5,120)   
        ])
def testa_fatorial(entrada, esperado):
    assert fatorial(entrada) == esperado
    
    
    
# a base da recursão é o caso base, que é o conjunto de reduções do problema em instâncias menores. O caso base é a condição de parada que define quando a recursão 
# deve terminar e a função deve começar a retornar valores para seus chamadores.

# Ao chamar a função recursiva, ela irá se chamar várias vezes com entradas menores do que a entrada original, até chegar ao caso base. A partir do caso base, a 
# função começará a retornar valores para os chamadores, que serão usados para resolver as chamadas mais altas da pilha de chamadas.

# Por exemplo, na função fatorial(n), o caso base é quando n = 0 ou n = 1, e a função retorna 1. Para calcular o fatorial de um número maior do que 1, a função 
# chama a si mesma com um número menor até chegar ao caso base. Dessa forma, a base da recursão é o caso base em que a função não chama mais a si mesma e começa 
# a retornar valores para resolver as chamadas mais altas da pilha de chamadas.