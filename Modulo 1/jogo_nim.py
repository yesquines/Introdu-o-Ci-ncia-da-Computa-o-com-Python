def computador_escolhe_jogada(n, m):
    print("")
    retirada = 0
    if (n % (m+1) == 0) or n == m:
        retirada = m
    else:
        while (n % (m+1) != 0):
            n = n - 1
            retirada = retirada + 1
    if retirada == 1:
        print("Computador tirou uma peça")
    else:
        print("Computador tirou", retirada,"peças")
    return retirada

def usuario_escolhe_jogada(n, m):
    print("")
    retirada = int(input("Quantas peças você vai retirar? "))
    while retirada > m or retirada > n or retirada <= 0:
        print("")
        print("Oops! Jogada inválida! Tente de novo.")
        print("")
        retirada = int(input("Quantas peças você vai retirar? "))
    if retirada == 1:
        print("Você tirou uma peça")
    else:
        print("Você tirou", retirada,"peças")
    return retirada
        
def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    if n <= 0 or m <= 0:
        print("Oops! Valores inválida! Tente de novo.")
        print("")
        partida()
    if (n % (m+1) == 0):
        print("")
        print("Você Começa!")
        ultimojogador = "Você"
        retirada = usuario_escolhe_jogada(n, m)
        n = n - retirada
        if n == 0:
                print("Fim do jogo! Você ganhou!")
                return "v"
        else:
                print("Agora resta apenas", n, "peças no tabuleiro")
    else:
        print("")
        print("Computador Começa!")
        ultimojogador = "Computador"
        retirada = computador_escolhe_jogada(n, m)
        n = n - retirada
        if n == 0:
                print("Fim do jogo! O computador ganhou!")
                return "c"
        else:
                print("Agora resta apenas", n, "peças no tabuleiro")
                
    while n > 0:
        if ultimojogador == "Você":
            retirada = computador_escolhe_jogada(n, m)
            n = n - retirada
            if n == 0:
                print("Fim do jogo! O computador ganhou!")
                return "c"
            else:
                print("Agora resta apenas", n, "peças no tabuleiro")
                ultimojogador = "Computador"
        else:
            retirada = usuario_escolhe_jogada(n, m)
            n = n - retirada
            if n == 0:
                print("Fim do jogo! Você ganhou!")
                return "v"
            else:
                print("Agora resta apenas", n, "peças no tabuleiro")
                ultimojogador = "Você"
                
def campeonato():
    i = 1
    c = 0
    v = 0
    while i <= 3:
        print("")
        print("**** Rodada ", i, " ****")
        print("")
        vencedor = partida()
        if vencedor == "c":
            c = c + 1
        else:
            v = v + 1
        i = i + 1
    print("")
    print("**** Final do campeonato! ****")
    print("")
    print("Placar: Você ",v,"X",c," Computador")
    
print("Bem-vindo ao jogo do NIM! Escolha:")
print("")
print("1 - para jogar uma partida isolada")
escolha = int(input("2 - para jogar um campeonato "))

if escolha == 1:
    print("")
    print("Você escolheu uma partida")
    partida()
else:
    if escolha == 2:
        print("")
        print("Você escolheu um campeonato")
        campeonato()
