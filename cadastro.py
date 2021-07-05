from datetime import datetime
import pandas as pd


##################################################
anuncio = []
def cadastro():
    nome = input('Digite o nome do anúncio: ')
    cliente = input('Digite o nome do cliente: ')
    # Data final
    d2 = datetime.strptime(input(f'Digite a data de início:'), '%d-%m-%Y')

    # Data inicial
    d1 = datetime.strptime(input(f'Digite a data de término:'), '%d-%m-%Y')
    quantidade_dias = abs((d2 - d1).days) + 1

    investimentoTotal = int(input('Digite o valor do investimento total: '))
    investimentoDiario = investimentoTotal / quantidade_dias
    anuncio.append((nome, cliente, d2, d1, f'{quantidade_dias} dias', investimentoDiario))
    #dados = pd.DataFrame(anuncio)
    print(anuncio)
    """ print(dados) ""

dados = []
def visualizar():
    dados = pd.DataFrame(anuncio, columns=['NomeAnúncio', 'Cliente', 'DataInício', 'DataFinal', 'Quant.Dias', 'Invest.Diário'])
    print(dados)


def filtro():
    dados = pd.DataFrame(anuncio, columns=['NomeAnúncio', 'Cliente', 'DataInício', 'DataFinal', 'Quant.Dias', 'Invest.Diário'])
    dados = dados[[input()]]
    print(dados)



#def filtrar():

while True:
    menu = int(input('''
    Deseja:
        [1] - Cadastrar
        [2] - Visualizar
        [3] - Filtrar
        [4] - Sair
                '''))


    if menu == 1:
        cadastro()
    elif menu == 2:
        visualizar()
    elif menu == 3:
        filtro()
    elif menu ==4:
        break


""" quantidade máxima de visualizações

quantidade máxima de cliques

quantidade máxima de compartilhamentos """



""" import datetime
from datetime import datetime

i = '2017/05/05'
f = '2017/05/01'

# Data final
d2 = datetime.strptime(input(f'Digite:'), '%Y-%m-%d')

# Data inicial
d1 = datetime.strptime(input(f'Digite:'), '%Y-%m-%d')

# Calculo da quantidade de dias
quantidade_dias = abs((d2 - d1).days) + 1
print(quantidade_dias) """