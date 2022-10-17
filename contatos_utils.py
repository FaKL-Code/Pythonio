import csv
from contato import Contato

def csv_contatos(arquivo, encoding = 'latin_1'):
    contatos = []
    
    with open(f'dados/{arquivo}.csv', encoding = encoding) as file:
        reader = csv.reader(file)

        for linha in reader:
            
            id, nome, email = linha
            
            contato = Contato(id, nome, email)
            contatos.append(contato)
    
    return contatos