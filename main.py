import posto as pt
from dados import*

combustiveis = le_combustiveis('combustiveis.csv')
frentista = le_frentistas('frentistas.csv')

print('Bem-vindo ao sistema de controle de vendas do posto!')

nomePosto = input('Digite o nome do posto: ')
salarioFixo = float(input('Digite o salario fixo do frentista: '))

postoDados = pt.cadastro_posto(nomePosto, salarioFixo, combustiveis, frentista)

pt.abastecer('Renan', 'gasolina', 300, postoDados)

while True:
    le_txt('dialogo.txt')
    try: 
        op = int(input('Digite o numero da operação que deseja realizar: '))
    except: 
        continue