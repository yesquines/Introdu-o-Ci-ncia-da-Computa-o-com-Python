def incomodam(n):
    if n > 0 and n < 2:
        return "incomodam "
    elif n >= 2: 
        return "incomodam " + incomodam(n-1)
    else:
        return ""

def elefantes(n):
    if n == 1:
        return "Um elefante " + incomodam(1) + "muita gente\n"
    if n > 0:
            return elefantes(n-1) + str(n) + " elefantes " + incomodam(n) + "muito mais\n" + str(n) + " elefantes " + incomodam(n) + "muita gente\n"
    else:
        return ""
