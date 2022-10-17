contato_a = '5, aaaaaaaaaaaaaaaaaaaaaaaaaaaa, aaaaaaaaaaaaaa@aaaaaaaaaaa.aaa.aa'
contato_b = '6, bbbbbbbbbbbbbbbbbbbbbbbbbbbb, bbbbbbbbbbbbbb@bbbbbbbbbbb.bbb.bb'

with open('dados/escrita.csv', 'w') as file:
    file.write(contato_a)    
with open('dados/escrita.csv', 'w') as arquivo:
    arquivo.write(contato_b)

file.write(contato_a)
arquivo.write(contato_b)

file.close()
arquivo.close()