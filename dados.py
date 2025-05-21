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

import pandas as pd

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

if __name__ == '__main__':    # Somente executa se o arquivo for chamado diretamente
    print(le_frentistas('frentistas.csv'))
    le_combustiveis('combustiveis.csv')