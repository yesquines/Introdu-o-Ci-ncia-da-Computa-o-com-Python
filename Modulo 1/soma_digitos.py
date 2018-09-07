num = int(input("Digite um número inteiro: "))
string = str(num)
soma = 0
i = 0
while i <= len(string):
    soma = soma + (num % 10)
    num = (num // 10)
    i+=1
print(soma)
