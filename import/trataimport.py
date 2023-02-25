from trataString import fazAlgo

if __name__ == "__main__":
    print(fazAlgo("teste"))
    print(fazAlgo("o ovo do avestruz"))
    print(fazAlgo("A CASA MUITO ENGRAÇADA"))
    print(fazAlgo("A TELEvisão queBROU"))
    print(fazAlgo("A Vaca Amarela"))
    
    
#     A instrução if __name__ == "__main__": é comumente usada em Python para indicar que um determinado trecho de código deve ser executado 
#     somente quando o script Python é executado diretamente e não quando ele é importado como um módulo em outro script.

# Isso ocorre porque, quando um módulo é importado em outro script Python, o Python define uma variável chamada __name__ com o nome do módulo. 
# No entanto, quando um script Python é executado diretamente, a variável __name__ é definida como "main".

# Portanto, a instrução if __name__ == "__main__": verifica se o script está sendo executado diretamente ou importado como um módulo em outro script e, 
# neste caso, o bloco de código dentro do if é executado. No caso do código que você mostrou, o bloco de código imprime o resultado da função fazAlgo() 
# com alguns argumentos de teste.




# entao como eu importei usando isso: from trataString import fazAlgo

# if __name__ == "__main__":
#     print(fazAlgo("teste"))
#     print(fazAlgo("o ovo do avestruz"))
#     print(fazAlgo("A CASA MUITO ENGRAÇADA"))
#     print(fazAlgo("A TELEvisão queBROU"))
#     print(fazAlgo("A Vaca Amarela")) . essa linha é desnecessaria? if __name__ == "__main__":

# Não, a linha if __name__ == "__main__": não é desnecessária. Na verdade, ela é uma boa prática de programação para garantir 
# que o código dentro dela só será executado se o módulo estiver sendo executado diretamente como um script.

# Se um módulo for importado em outro script Python, o código dentro do bloco if __name__ == "__main__": não será executado. 
# Dessa forma, é possível ter trechos de código que são executados apenas se o módulo estiver sendo executado diretamente e 
# outros trechos que são usados apenas quando o módulo é importado em outros scripts.