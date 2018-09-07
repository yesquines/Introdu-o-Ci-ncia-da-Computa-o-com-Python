def bubble_sort(lista):
    if len(lista) != 1:
        for i in range(len(lista)-1, 0, -1):
            for k in range(i):
                if lista[k] > lista[k+1]:
                    lista[k],lista[k+1] = lista[k+1],lista[k]
            print(lista)
            if lista == sorted(lista):
                return lista
    else:   
        return lista
