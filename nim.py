#A função recebe dois parâmetros: n, que representa o número de peças no tabuleiro, e m, que é o número máximo de peças que pode ser retirado em uma jogada.


def computador_escolhe_jogada(n, m):
    if n % (m + 1) == 0:
        return m  # o computador pode retirar o máximo de peças
    else:
        return n % (m + 1) # o computador retira as peças necessárias para deixar um múltiplo de (m + 1)
    
def usuario_escolhe_jogada(n, m):
    jogada_valida = False
    while not jogada_valida:
        jogada = int(input("Quantas peças você vai tirar? "))
        if jogada < 1 or jogada > m or jogada > n:
            print("Jogada inválida!")
        else:
            jogada_valida = True
    return jogada


def jogar_partida():
    print("Você escolheu uma partida!")
    
def jogar_campeonato():
    jogador = 0
    placar_jogador = 0
    placar_computador = 0

    for i in range(3):
        print("**** Rodada", i+1, "****\n")
        vencedor = partida()
        if vencedor == 1:
            placar_jogador += 1
        else:
            placar_computador += 1
    
    print("**** Final do campeonato ****\n")
    print("Placar: Você", placar_jogador, "X", placar_computador, "Computador")
    if placar_jogador > placar_computador:
        print("Você ganhou o campeonato!")
    elif placar_jogador < placar_computador:
        print("O computador ganhou o campeonato!")
    else:
        print("O campeonato terminou empatado!")
    
def partida():
    print("Bem-vindo ao jogo do NIM!")

    escolha = int(input("Escolha uma opção:\n1 - para jogar uma partida isolada\n2 - para jogar um campeonato\n"))
    if escolha == 1:
        jogar_partida()
    elif escolha == 2:
        jogar_campeonato()
    else:
        print("Opção inválida.")
        
        
    n =int(input("Informe o número de peças inicial "))
    m = int(input("Limite de peças por jogada? "))
    
    if n % (m + 1) == 0:
        print("Você começa!")
        jogador = 1
    else:
        print("Computador começa!")
        jogador = 0

    while n > 0:
        if jogador == 0:
            jogada = computador_escolhe_jogada(n, m)
            jogador = 1
        else:
            jogada = usuario_escolhe_jogada(n, m)
            jogador = 0
            print("\nVocê tirou", jogada, "peça(s).")

        n -= jogada
        print("Agora restam", n, "peça(s) no tabuleiro.\n")

    if jogador == 0:
        print("O computador ganhou!")
    else:
        print("Você ganhou!")


partida()