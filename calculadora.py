print('\nCalculadora de alcance de anúncio online.\n')

# Estimativa de investimento
investimento = int(input('Digite o valor do investimento sugerido: '))

print('-' * 50)

# Número total de visualizações do anúncio original
views_origin = investimento * 30
print(f'O número de visualizações a cada 1 real investido foi de {views_origin} pessoas.')

# Número de cliques a cada 100 visualizações
cliques = (views_origin // 100) * 12
print(f'O numero de cliques a cada 100 visualizações foi de {cliques} cliques no anúncio.')

# Número de compartilhamento acada 20 cliques no anúncio
compartilhamento = (cliques // 20) * 3
print(f'Das {cliques} pessoas que clicaram mo anúncio, {compartilhamento} pessoas compartilharam.')

# Número total de compartilhamentos de uma sequência máxima de 4
maxCompartilhamento = compartilhamento * 4

# Número total de visualizações da sequência máxima de 4 compartilhamentos
newsViews = maxCompartilhamento * 40

# Cálculo de cada compartilhamento gerando 40 novas views 
newsViews = compartilhamento * 40
print(f'Foram geradas {newsViews} novas visualizações a partir dos compartilhamentos.')

print('-' * 50)

# Quantidade máxima de pessoas que visualizarão o mesmo anúncio
projecaoVisualizacoes = views_origin + newsViews
print(f'A projeção aproximada é de {projecaoVisualizacoes} visualizações.')


#Parte 2
import datetime
import pandas as pd


#fimAnuncio = datetime.date(input('Digite a data de finalização do anúncio: '))
""" diaF = int(input('Digite dia final do anúncio: '))
mesF = int(input('Digite mês final do anúncio: '))
anoF = int(input('Digite ano final do anúncio: '))
#investimento 

dataInicio = datetime.date(day= diaI, month= mesI,year= anoI)
dataFim = datetime.date(day= diaF, month= mesF,year= anoF)


dias_de_anuncio = (dataFim - dataInicio).days + 1
print(dias_de_anuncio) """
##################################################
""" anuncio = []
def cadastro():
    nome = input('Digite o nome do anúncio: ')
    cliente = input('Digite o nome do cliente: ')
    diaI = int(input('Digite o dia de início do anúncio: '))
    mesI = int(input('Digite o mês de início do anúncio: '))
    anoI = int(input('Digite o ano de início do anúncio: '))
    diaF = int(input('Digite dia final do anúncio: '))
    mesF = int(input('Digite mês final do anúncio: '))
    anoF = int(input('Digite ano final do anúncio: '))  
    dataInicio = datetime.date(day= diaI, month= mesI,year= anoI)
    dataFim = datetime.date(day= diaF, month= mesF,year= anoF)
    dias_de_anuncio = (dataFim - dataInicio).days + 1
    investimentoTotal = int(input('Digite o valor do investimento sugerido: '))
    investimentoDiario = investimentoTotal / dias_de_anuncio
    anuncio.append((nome, cliente,f'{diaI}/{mesI}/{anoI}', f'{diaF}/{mesF}/{anoF}', f'{dias_de_anuncio} dias', investimentoDiario))
    #dados = pd.DataFrame(anuncio)
    print(anuncio)
    print(dados)

dados = []
def ver():
    dados = pd.DataFrame(anuncio)
    print(dados)

#def filtrar():

while True:
    menu = int(input('''
    Deseja:
        [1] - Cadastrar
        [2] - Visualizar
        [3] - Sair
                '''))


    if menu == 1:
        cadastro()
    elif menu == 2:
        ver()
    elif menu == 3:
        break
 """

""" quantidade máxima de visualizações

quantidade máxima de cliques

quantidade máxima de compartilhamentos """