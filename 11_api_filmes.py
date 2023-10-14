import requests
import json

req = None
def requisicao(titulo):
  try:
    req = requests.get('https://www.omdbapi.com/?apikey=47e845da&t=' + titulo)
    dict = json.loads(req.text)
    return dict
  except:
    print('Erro na conexão')
    return None
  
def printDetalhes(filme):
  print('Título:',filme['Title'])
  print('Ano:',filme['Year'])
  print('Diretor:',filme['Director'])
  print('Atores:',filme['Actors'])
  print('Nota:',filme['imdbRating'])
  print('Prêmios:',filme['Awards'])
  print('Poster:',filme['Poster'])
  
sair = False
while not sair:
  op = input('Escreva o nome de um filme ou SAIR para fechar: ')

  if op == 'SAIR':
    sair = True
    print('Saindo...')
  else:
    filme = requisicao(op)
    if filme['Response'] == 'False':
      print("Filme não encontrado")
    else:
      printDetalhes(filme)



