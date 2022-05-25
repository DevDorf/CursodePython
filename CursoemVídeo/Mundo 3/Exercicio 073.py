times = 'santos', 'palmeiras', 'corinthians', 'são paulo', 'internacional',\
        'atletico mineiro', 'cruzeiro', 'chapecoense', 'remo', 'paysandu',\
        'vasco', 'flamengo', 'coritiba', 'botafogo', 'bahia', 'vitória',\
        'fluminense', 'goias', 'sport', 'portuguesa'
print(f'Times do Brasileirão: {times}')
print('-=-' * 20)
for c in range(0, 6):
    print(f'Os cinco primeiros times {times[c]}')
# print(f'Os cinco primeiros times {times[0:5]}')
print('-=-' * 20)
print(f'Os 4 ultimos colocados são: {times[-4:]}')
print('-=-' * 20)
print(f'Em ordem alfabética {sorted(times)}')
print('-=-' * 20)
print(f'O time da chapecoense esta em {times.index("chapecoense") + 1}ª posição')
