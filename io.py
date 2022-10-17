#file = open('dados/contatos.csv')
file = open('dados/escrita.csv', 'w')

#print(type(file.buffer))

#content = file.buffer.read()

#print(content)

#texto = bytes('Isso é um texto em bytes')
#texto_bytes = b'Isso e um texto em bytes'
#print(texto_bytes)

contato = bytes('13, ggggggggggggggg, ggggggggggggggggg@gggggggg.ggg.gg\n', 'latin_1')

file.buffer.write(contato)

file.close()