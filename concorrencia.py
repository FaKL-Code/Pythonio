file = open('dados/escrita.csv', 'w')
arquivo = open('dados/escrita.csv', 'w')

contato_a = '5, aaaaaaaaaaaaaaaaaaaaaaaaaaaa, aaaaaaaaaaaaaa@aaaaaaaaaaa.aaa.aa'
contato_b = '6, bbbbbbbbbbbbbbbbbbbbbbbbbbbb, bbbbbbbbbbbbbb@bbbbbbbbbbb.bbb.bb'

file.write(contato_a)
arquivo.write(contato_b)

file.close()
arquivo.close()