def maiusculas(frase):
    maiusc = ""
    i = 0
    for i in range(len(frase)):
        if (ord(frase[i]) >= 66 and ord(frase[i]) <= 90):
            maiusc = maiusc + frase[i];
    
    return maiusc
