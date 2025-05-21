import posto as pt
from dados import*

combustiveis = le_combustiveis('combustiveis.csv')
frentistas = le_frentistas('frentistas.csv')

print('Bem-vindo ao sistema de controle de vendas do posto!')

nomePosto = input('Digite o nome do posto: ')
salarioFixo = float(input('Digite o salario fixo do frentista: '))

postoDados = pt.cadastro_posto(nomePosto, salarioFixo, combustiveis, frentistas)


def operacao(op, postoDados):
    if op == 1: #abastecer
        frentista = input('Digite o nome do frentista: ')
        combustivel = input('Digite o combustivel: ')
        valor = float(input('Digite o valor que o cliente deseja abastecer: '))
        pt.abastecer(frentista, combustivel, valor, postoDados)
        return 'Abastecimento realizado com sucesso!'  
    elif op == 2:
        if postoDados['bloqueado']:
            return 'O posto ja esta bloqueado!'
        else:
            postoDados['bloqueado'] = True
            return 'O posto acaba de ser bloqueado!'
    elif op == 3:
        if not postoDados['bloqueado']:
            return 'O posto ja esta desbloqueado!'
        else:
            postoDados['bloqueado'] = False
            return 'O posto acaba de ser desbloqueado!'
    elif op == 4:
        relatorio('relatorio 01',postoDados) 

nome_relatorio = 'relatorio 01'

while True: 
    le_txt('dialogo.txt')

    try: 
        op = int(input('Digite o numero da operação que deseja realizar: '))
    except: 
        continue
    if op ==5:
        break
    
    resposta = operacao(op, postoDados)
    print(resposta)
    
print('Sistema encerrado!')