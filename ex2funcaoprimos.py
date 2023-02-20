def encontrar_primo(num):
  for n in range(num, 1, -1):  #O loop for n in range(num, 1, -1) foi adicionado para iterar de forma decrescente, de num até 2, ou seja, começando pelo número fornecido e indo até o menor número primo possível. 
                                #Essa abordagem ajuda a encontrar o maior número primo dentro do intervalo especificado com mais eficiência, porque quando o primeiro número primo é encontrado, ele será retornado como o maior número primo e o loop será interrompido, não sendo necessário percorrer o restante do intervalo.
   divisores = 0                #Se o loop iterasse de forma crescente, a função precisaria verificar todos os números entre 2 e num para encontrar o maior número primo, o que seria menos eficiente.
  for divisor in range(1, n+1):
    if n % divisor == 0:
        divisores = divisores + 1
        if divisores > 2:
          break
        if divisores == 2:
            return n
    return None
    
    maximo = encontrar_primo(num)
    if maximo is None:
        print(f"Não foi encontrado nenhum número primo entre 2 e {num}.")
    else:
        print(f"O maior número primo entre 2 e {num} é {maximo}.")