from datetime import datetime
import pandas as pd

print('\nSistema de cadastro de anúncios.\n')
anuncio = []

# Função para cadastrar
def cadastro():
    nome = input('Digite o nome do anúncio: ')
    cliente = input('Digite o nome do cliente: ')
    # Data inicial
    dataInicio = datetime.strptime(input(f'Digite a data de início (dd-mm-aaaa):'), '%d-%m-%Y')

    # Data final
    dataFim = datetime.strptime(input(f'Digite a data de término (dd-mm-aaaa):'), '%d-%m-%Y')
    quantidade_dias = abs((dataFim - dataInicio).days) + 1

    investimentoTotal = int(input('Digite o valor do investimento total: '))
    investimentoDiario = investimentoTotal / quantidade_dias
    anuncio.append((nome, cliente, dataInicio, dataFim, f'{quantidade_dias} dias', investimentoDiario))



# Função para visualizar cadastros
def visualizar():
    dados = pd.DataFrame(anuncio, columns=['NomeAnúncio', 'Cliente', 'DataInício', 'DataFinal', 'Quant.Dias', 'Invest.Diário'])
    print(dados)



# Função para filtrar
def filtro():
    dados = pd.DataFrame(anuncio, columns=['NomeAnúncio', 'Cliente', 'DataInício', 'DataFinal', 'Quant.Dias', 'Invest.Diário'])
    dados = dados.loc[dados['Cliente'] == input(f'Digite o nome do cliente: ')]
    print(dados)



# Funcionamento do sistema
while True:
    menu = int(input('''
    Deseja:
        [1] - Cadastrar Anúncios
        [2] - Visualizar Anúncios
        [3] - Filtrar por Cliente
        [4] - Sair
                '''))


    if menu == 1:
        cadastro()
    elif menu == 2:
        visualizar()
    elif menu == 3:
        filtro()
    elif menu ==4:
        print('Cadastros finalizados.')
        break

