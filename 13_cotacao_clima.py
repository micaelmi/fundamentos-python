import requests
import json

dolar = 'https://economia.awesomeapi.com.br/last/USD-BRL'
clima = 'https://api.hgbrasil.com/weather'

print("O que você deseja saber?")
req = int(input("1 - Cotação do dólar \n2 - Previsão do tempo\nDigite: "))

tipo = ""
if req == 1:
  tipo = dolar
  requisicao = requests.get(tipo)
  cotacao = json.loads(requisicao.text)
  # print(requisicao.text)
  print("1 Dólar =", cotacao["USDBRL"]["bid"], "reais")
else:
  tipo = clima
  requisicao = requests.get(tipo)
  previsao = json.loads(requisicao.text)
  # print(requisicao.text)
  print("Data: ", previsao["results"]["date"])
  print("Temperatura: ", previsao["results"]["temp"], "°C")
  print(previsao["results"]["description"])
  print("Vento: ", previsao["results"]["wind_speedy"])
  

