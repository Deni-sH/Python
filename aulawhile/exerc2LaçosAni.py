# Refaça o exercício 1 imprimindo os retângulos sem preenchimento, de forma que os caracteres que não estiverem na borda do retângulo sejam espaços.

# Por exemplo:
    
    
# digite a largura: 10
# digite a altura: 3
#   ##########
#   #        #
#   ##########

largura = int(input("digite a largura: ")) 
altura = int(input("digite a altura: "))

i = 0
while i < altura:
    j = 0
    while j < largura:
        if i == 0 or i == altura - 1 or j == 0 or j == largura - 1:
            print("#", end="")
        else:
            print(" ", end="")
        j = j+1
    print()   
    i = i + 1