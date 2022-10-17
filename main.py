import contatos_utils

try:
    contatos = contatos_utils.csv_contatos('contatos')
    
    for contato in contatos:
        print(f'{contato.id} - {contato.nome} - {contato.email}')
except FileNotFoundError:
    print('arquivo nao encontrado')
except PermissionError:
    print('Sem permissao para escrever no diretorio')