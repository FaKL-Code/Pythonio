file = open('dados/escrita.csv', 'a+')

contato = ['4, dddddddddddddddddd, dddddddddddd@ddddddddd.ddd.dd\n']

for pessoa in contato:
    file.write(pessoa)

file.flush()

file.seek(0)

for linha in file:
    print(linha)

file.close()