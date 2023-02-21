# Nesta lista de exercícios vamos praticar os conceitos vistos até agora.  Cada exercício deve ser resolvido 
# em um arquivo separado e a seguir  enviado através da web. A correção automática pode demorar alguns  minutos. 
# Você pode submeter a mesma resposta mais de uma vez caso  perceba que a resposta anterior tinha algum problema;
# a última versão é a  que vale.

# Seja preciso quando valores de retorno pedidos forem cadeias de caracteres.

# Exercício 1 - FizzBuzz
# Escreva a função fizzbuzz que recebe como parâmetro um número inteiro e devolve

# 'Fizz' se o número for divisível por 3 e não for divisível por 5;

# 'Buzz' se o número for divisível por 5 e não for divisível por 3;

# 'FizzBuzz' se o número for divisível por 3 e por 5;

# Caso o número não seja divisível 3 e também não seja divisível por 5, ela deve devolver o número recebido como parâmetro.

# Exemplos de execução no Python Shell

# >>>fizzbuzz(3)
# "Fizz"
# >>>fizzbuzz(5)
# "Buzz"
# >>>fizzbuzz(15)
# "FizzBuzz"
# >>>fizzbuzz(4)
# 4


def fizzbuzz(num):
    resultados = []
    for n in range(1, num+1):
        if(n % 3 == 0 and n % 5 != 0):
            resultados.append("Fizz")
        elif(n % 5 == 0 and n % 3 != 0):
            resultados.append("Buzz")
        elif(n % 5 == 0 and n % 3 == 0):
            resultados.append("FizzBuzz")
        else:
            resultados.append(str(n))
    return resultados[num-1]

print(fizzbuzz(15))


def test_fizzbuzz():
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(4) == "4"

    # Outros testes possíveis
    assert fizzbuzz(1) == "1"
    assert fizzbuzz(2) == "2"
    assert fizzbuzz(6) == "Fizz"
    assert fizzbuzz(10) == "Buzz"
    assert fizzbuzz(30) == "FizzBuzz"






#"resultado" é uma variável que pode ser usada para armazenar o valor retornado por uma função ou para armazenar um valor intermediário em um programa.

# A função append é um método em Python que permite adicionar elementos a uma lista existente. 
# Quando você chama lista.append(elemento) em uma lista lista, elemento é adicionado ao final da 
# lista. Isso é útil quando você precisa adicionar novos elementos dinamicamente a uma lista existente.