import contatos_utils

try:
    contatos = contatos_utils.csv_contatos('contatos')
#    contatos_utils.pickle_contatos(contatos, 'contatos')

#    contatos = contatos_utils.converter_pickle('contatos')
#    contatos_utils.json_contatos(contatos, 'contatos')

    contatos = contatos_utils.converter_json('contatos')
    
    for contato in contatos:
        print(f'{contato.id} - {contato.nome} - {contato.email}')
except FileNotFoundError:
    print('arquivo nao encontrado')
except PermissionError:
    print('Sem permissao para escrever no diretorio')