# estruturas-de-dados

lista = ['farinha', 'ovo', 'açucar', 'leite'] # manipulavel (list)

tupla = ('farinha', 'ovo', 'açucar', 'leite') # imutavel    (tuple)

conjunto = {'farinha', 'ovo', 'açucar', 'leite'} # não repete itens, não ordenado (set)

dicionario = {
  'nome': 'Micael',
  'idade': 19
  } # tipo um objeto json (dict)
  
dicionario['endereco'] = 'Piracaia'

if 'Micael' in dicionario.values():
  print('Micael esta no dicionario')
  
print("")
for chaves in dicionario.keys():
  print(chaves)
  
print("")
for valores in dicionario.values():
  print(valores)
  
print("") # Conjunto é bom para buscas
for item in conjunto:
  print(item)
  
print("\nBuscar ingrediente")
ingrediente = input("digite: ")
if ingrediente in conjunto:
  print('Foi encontrado no conjunto')
else:
  print('Ingrediente não encontrado')
  
lista = []
tupla = ()
dicionario = {}
conjunto = set()

loucura = [(1,2,3), (4,5,6), ({'arroz', 'feijão'}, {'carne', 'frango'})]

print(loucura)