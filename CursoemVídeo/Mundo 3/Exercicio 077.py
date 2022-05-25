tupla = 'caio', 'camila', 'gustavo', 'felipe', 'joao',\
        'erick', 'jose', 'fernando', 'pedro'
for c in tupla:
    print(f'\nNa palavra {c.upper()} temos ', end='')
    for letra in c:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
