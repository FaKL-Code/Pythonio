file = open('dados/contatos.csv')

print(type(file.buffer))

content = file.buffer.read()

print(content)

texto = bytes('Isso é um texto em bytes')
texto_bytes = b'Isso e um texto em bytes'
print(texto_bytes)

file.close()