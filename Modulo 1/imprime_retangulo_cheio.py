largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))
linhas = 1
colunas = 1
while linhas <= altura:
    while colunas <= largura:
            print("#", end='')
            colunas = colunas + 1
    print("")
    linhas = linhas +1
    colunas = 1
