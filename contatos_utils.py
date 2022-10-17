import csv, pickle, json
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

def json_contatos(contatos, arquivo):
    with open(f'dados/{arquivo}.json', 'w') as file:
        json.dump(contatos, file, default = contato_json)
        
def contato_json(contato):
    return contato.__dict__
        
def converter_json(arquivo):
    contatos = []
    
    with open(f'dados/{arquivo}.json', 'r') as file:
        contato_dicionario = json.load(file)
        
        for contato in contato_dicionario:
            c = Contato(**contato)
            contatos.append(c)
  
    return contatos