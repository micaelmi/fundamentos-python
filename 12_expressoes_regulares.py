import re
import requests

print("+**********************************************+")
print("               Buscador de e-mails              ")
site = input("Informe o site que você deseja buscar um e-mail:\n")
req = requests.get(site)

padrao = re.findall(r'[\w-]+@[\w-]+\.[\w\.-]+', req.text) 
# re.findall() -> procura todas as ocorrencias na string
# re.search() -> verifica se atende aos critérios e retorna o encontrado
# r'' -> RAW STRING: ignora caracteres especiais (tipo \n, não pula a linha)
# '\w' -> verifica se existe um caractere do tipo word (palavra)
# a{4,6} -> procura ocorrencias de 4 a 6 letras "a" seguidas

if padrao:
  print(padrao)
  # padrao.group() se for utilizado o metodo search
else:
  print("E-mail não encontrado")