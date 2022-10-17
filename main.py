try:
    with open('dados/contatos.csv') as file:

        for linha in file:
            print(linha)
except FileNotFoundError:
    print('arquivo nao encontrado')
except PermissionError:
    print('Sem permissao para escrever no diretorio')