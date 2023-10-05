import time

try:
  a = 10 / 0
except ZeroDivisionError:
  print("Divisão por zero, não dá pra fazer")
except NameError:
  print("Você digitou alguma coisa errada")
except Exception as erro:
  print("Erro", erro)
  
def abreArquivo():
  try:
    arquivo = open('arquivo-x.txt')
    return True
  except Exception as erro:
    print("Erro", erro)
    return False
  
while not abreArquivo():
  print('tentando abrir arquivo')
  time.sleep(5)

print('arquivo aberto!!')