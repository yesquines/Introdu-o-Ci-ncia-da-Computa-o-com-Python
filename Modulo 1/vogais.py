def vogal(x):
    vogais = ['a','e','i','o','u']
    if x.lower() in vogais:
        return True
    else:
        return False

v = input('Digite uma vogal: ')

print(vogal(v))
