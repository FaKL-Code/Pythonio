import csv, pickle
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

def pickle_contatos(contatos, arquivo):
    with open(f'dados/{arquivo}.p', 'wb') as file:
        pickle.dump(contatos, file)
        
def converter_pickle(arquivo):
    with open(f'dados/{arquivo}.p', 'rb') as file:
        contatos = pickle.load(file)
    
    return contatos