def maior_primo(x):
    if x >= 2:
        i = 1
        j = 1
        primo = 0
        while i <= x:
            while j <= x:
                if j % i == 0:
                    j = j+1
                else:
                    if j > primo:
                        primo = j
                        j = j+1
                    else:
                        j = j+1
            i = i+1
            j = 0
    return primo    
