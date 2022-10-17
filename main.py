try:
    file = open('dados/contatos.csv')

    for linha in file:
        print(linha)

finally:
    file.close()