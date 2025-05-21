'''
combustivel = {
    'gasolina': {   
        'preco': 5.79,
        'volume': 500
    },
    'etanol' : {
        'preco': 4.07,
        'volume': 200
    }
}
'''

# frentist = {
#     'nome' : {
#     'num_vendas' : 0,
#     'bonus' : 0
#     },
# }
import datetime as dt
import pandas as pd

def le_txt(arquivo):
    with open(arquivo, 'r') as file:
        print(file.read())

def le_combustiveis(arquivo):
    combustiveis = {}
    dados_combustiveis = pd.read_csv(arquivo)
    dados_combustiveis = dados_combustiveis.to_dict('records') # Converte o DataFrame em uma lista de dicionários, records trasforma o DataFrame em uma lista de dicionários
    for dados in dados_combustiveis:
        combustiveis[dados['nome']]={
            'preco' : dados['preco'],
            'volume' : dados['volume']
        }
    return combustiveis
    
def le_frentistas(arquivo):
    frentistas = {}
    dados_frentistas = pd.read_csv(arquivo)
    dados_frentistas = dados_frentistas.to_dict('records')
    for dados in dados_frentistas:
        frentistas[dados['nome']] = {
            'num_vendas' : 0,
            'bonus' : 0
        }
    return frentistas

def relatorio(nome, posto_dados):
    nome += '.txt'
    with open(nome, 'w+') as file:
        file.write(f'Relatorio do posto {posto_dados["nome"]}\n\n')
        
        file.write('Combustiveis:\n')
        for combustivel in posto_dados['combustiveis'].items():
            file.write(f'Tipo: {combustivel[0]}\n\n')
            file.write(f"Disponivel: {combustivel[1]['volume']}\n\n")
            file.write(f"Preco atual: {combustivel[1]['preco']}\n\n")
        
        file.write('Frentistas:\n')
        for frentista in posto_dados['frentistas'].items():
            file.write(f'Nome: {frentista[0]}\n\n')
            file.write(f" - Bonus: {frentista[1]['bonus']}\n\n")
            
        file.write(f'Faturamento total: {posto_dados["faturamento"]}\n\n')
        
        file.write(f'Criado em: {dt.datetime.now()}')
        

if __name__ == '__main__':    # Somente executa se o arquivo for chamado diretamente
    print(le_frentistas('frentistas.csv'))
    le_combustiveis('combustiveis.csv')