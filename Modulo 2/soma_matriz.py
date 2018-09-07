def soma_matrizes(m1,m2):
    soma = [];
    for i in range(len(m1)):
        linha = [];
        for j in range(len(m1[i])):
            if len(m1[i]) == len(m2[i]):
                   linha.append(m1[i][j]+m2[i][j])
            else:
                return False
        soma.append(linha);
    return soma
    
                    
                            
