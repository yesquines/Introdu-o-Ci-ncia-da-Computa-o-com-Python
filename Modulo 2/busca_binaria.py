def busca(lista,x):
    p = 0
    u = len(lista)-1

    while p <= u:
        meio = (p + u) // 2
        if lista[meio] == x:
            return meio
        else:
            if x<lista[meio]:
                u = meio - 1
                print(meio)
            else:
                p = meio + 1
                print(meio)
    return False
