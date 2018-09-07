def remove_repetidos(lista):
    listafinal = []
    for i in range(len(lista)):
        if lista[i] not in listafinal:
            listafinal.append(lista[i])
    listafinal.sort()
    return listafinal
