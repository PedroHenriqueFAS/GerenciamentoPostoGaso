from dados import*

combustiveis = le_combustiveis('combustiveis.csv')
frentista = le_frentistas('frentistas.csv')

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

def cadastro_posto(nome_posto, salario_fixo, combustiveis=combustiveis, frentista=frentista):
    posto_dados = {
        'nome' : nome_posto,
        'combustiveis' : combustiveis,
        'frentistas': frentista,
        'faturamento' : 0,
        'bloqueado' : False,
        'salario_fixo' : salario_fixo
    }
    return posto_dados

def consumo(valor, combustivel, posto_dados):
    combustivel = posto_dados['combustiveis'][combustivel]
    consumido = valor / combustivel['preco']
    combustivel['volume'] -= consumido
    if combustivel['volume'] < 0:
        return False
    else:
        return float (f'{consumido["volume"]:.3f}')

def abastecer(frentistas, combustivel, valor,posto_dados):
    posto_dados['frentistas'][frentistas]['numero_vendas']=+1
    posto_dados['combustiveis'][combustiveis]['volume'] = consumo(valor, combustivel, posto_dados)
    
    if not posto_dados['combustiveis'][combustiveis]['volume'] == False:
        posto_dados['faturamento']+= valor
    else:
        return 'Nao foi possivel abastecer'