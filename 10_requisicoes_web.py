import requests # biblioteca para requisições web
# -> para instalar, rodar comando "pip install requests"

# Beautiful Soap 4 (bs4) -> biblioteca alternativa


header = {
  'User-agent': 'Windows 12',
  'Referer': 'https://google.com'
}

cookies = {
  'Ultima-visita': '05-10-2023'
}

dados = {
  'username': 'micaelmi',
  'password': '12345678'
}

texto = None

try:
  req = requests.get('https://putsreq.com/eW1p6c9asGuZq5TqXkFU', headers=header, cookies=cookies, data=dados)
  texto = req.text
  print(req.content)
except Exception as e:
  print("Erro na requisição", e)

print(texto)

