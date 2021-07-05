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
