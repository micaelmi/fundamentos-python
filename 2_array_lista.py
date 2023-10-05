lista = ['macarrao', 'molho', 'calabresa', 'bacon', 'queijo']

print(lista)
print(lista[2])
print(lista[-1])

lista.append('cebola')
lista.remove('queijo')
lista.append('parmesao')

print(lista)


lista.insert(2, 'molho')

print(lista.count('molho'))

print(lista)

print(len(lista))

print(lista.pop())
print(lista)

lista.clear()



frase = 'Howre You Doing?'

print(frase[15])
print(frase[0:5])
print(frase[0:10:2])

print(frase.lower())
print(frase.split(' '))