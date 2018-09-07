largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))
linhas = 1
colunas = 1
while linhas <= altura:
    while colunas <= largura:
            if colunas == 1 or colunas == largura:
                print("#", end='')
            else:
                if linhas == 1 or linhas == altura:
                    print("#", end='')
                else:
                    print(" ", end='')
            colunas = colunas + 1
    print("")
    linhas = linhas +1
    colunas = 1
