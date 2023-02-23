#A função recebe dois parâmetros: n, que representa o número de peças no tabuleiro, e m, que é o número máximo de peças que pode ser retirado em uma jogada.

def computador_escolhe_jogada(n, m):
    if n % (m+1) == 0:
        return 1
    else:
        return n % (m+1) 
    

def usuario_escolhe_jogada(n, m):
    jogada = int(input("Quantas peças você vai tirar? "))
    i = 0
    while jogada > m or jogada < 1 or jogada > n:
        print("Jogada inválida! Tente de novo.")
        jogada = int(input("Quantas peças você vai tirar? "))
        i = i +1
    return jogada

def campeonato():
    placar = [0, 0]
    
    for rodada in range(1, 4):
        print("**** Rodada", rodada, "****\n")
        resultado = partida()
        if resultado == 1:
            placar[0] += 1
        else:
            placar[1] += 1
        print("Placar: Você", placar[0], "X", placar[1], "Computador\n")
    print("**** Final do campeonato! ****\n")
    if placar[0] > placar[1]:
        print("Você ganhou o campeonato!")
    else:
        print("O computador ganhou o campeonato!")

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    vez_computer = False

    if n % (m+1) == 0:
        print()
        print("Voce começa!")

    else:
        print()
        print("Computador começa!")
        vez_computer = True

    while n > 0:
        if vez_computer:
            computador_remove = computador_escolhe_jogada(n, m)
            n -= computador_remove
            if computador_remove == 1:
                print()
                print("O computador tirou uma peça")
            else:
                print()
                print("O computador tirou", computador_remove, "peças")

            vez_computer = False
        else:
            jogadorRemove = usuario_escolhe_jogada(n, m)
            n -= jogadorRemove
            if jogadorRemove == 1:
                print()
                print("Você tirou uma peça")
            else:
                print()
                print("Você tirou", jogadorRemove, "peças")
            vez_computer = True
        if n == 1:
            print("Agora resta apenas uma peça no tabuleiro.")
            print()
        else:
            if n != 0:
                print("Agora restam,", n, "peças no tabuleiro.")
                print()
            
    print("Fim do jogo! O computador ganhou!")

tipo_jogo = int(input("Bem-vindo ao jogo do NIM! Escolha:\n\n1 - para jogar uma partida isolada\n2 - para jogar um campeonato\n"))

if tipo_jogo == 1:
    partida()
else:
    campeonato()
    
    
    
    # def usuario_escolhe_jogada(n, m):
    # jogada = int(input("Quantas peças você vai tirar? "))
    
    # while jogada > m or jogada < 1 or jogada > n:
    #     print("Jogada inválida! Tente de novo.")
    #     jogada = int(input("Quantas peças você vai tirar? "))
    # return jogada
    
    
