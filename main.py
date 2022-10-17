try:
    file = open('dados/contatos.csv')

    for linha in file:
        print(linha)
except FileNotFoundError:
    print('arquivo nao encontrado')
except PermissionError:
    print('Sem permissao para escrever no diretorio')
finally:
    file.close()