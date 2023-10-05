'''
parâmetros da função open():
w -> write (cria um novo arquivo e escreve nele)
r -> read (ler arquivo)
r+ -> leitura e escrita
a -> append (cria arquivo e adiciona conteudo)
b -> leitura binária, para arquivos que não são texto
 > passar outro parâmetro junto com o b, tipo wb ou rb
'''


arquivo = open('8_arquivos\\arquivo.txt', 'w')

arquivo.write("escrevendo no txt pelo Python!")

for i in range(0, 21):
  arquivo.write(str(i) + "\n")
  
arquivo2 = open('8_arquivos\\arquivo2.txt', 'r')

for i in arquivo2:
  print(i)
  