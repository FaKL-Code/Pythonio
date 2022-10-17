file = open('dados/escrita.csv', 'a')

contato = ['4, dddddddddddddddddd, dddddddddddd@ddddddddd.ddd.dd\n']

for pessoa in contato:
    file.write(pessoa)

file.flush()

file.write(contato)

file.close()