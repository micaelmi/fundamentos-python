# métodos e funções

def soma(n1, n2):
  return n1+n2

print('soma',soma(22.22,33.33))

def minimumChar(arg):
  if len(arg) > 5:
    return True
  else:
    return False
  
print(minimumChar('123456'))


'''
escreva uma função que recebe um objeto de coleção 
e retorna o valor do maior número dentro dela
'''

def findBiggest(collection):
  biggest = 0
  for number in collection:
    if number > biggest:
      biggest = number
  return biggest
    
numbers = {4,66,5,1,98,76,34,912,44,6,1,88,34,221}
print(numbers)
print('Maior número da coleção:', findBiggest(numbers))