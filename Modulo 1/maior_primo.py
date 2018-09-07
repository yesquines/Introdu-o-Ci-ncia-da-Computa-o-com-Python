def ePrimo(k):
  i = 1
  primo = 0
  while i <= k:
    c = 0
    j = 1
    while j <= i:
      if i % j == 0:
        c = c + 1
      j = j+1
    if c == 2:
      if i > primo:
        primo = i
    i = i+1
  return primo
  
def maior_primo(x):
  if x >= 2:
    return ePrimo(x)
