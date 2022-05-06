print('Calculadora de alistamento')
ano_nasc = int(input('Em que ano você nasceu? '))
idade = 2022 - ano_nasc

if idade < 18:
    falta = 18 - idade
    print(f'Se deu bem, ainda falta {falta} anos para se alistar')
elif idade == 18:
    print('Se ferrou, vai se alistar rapaz!')
elif idade > 18:
    alist = input('Você já se alistou?\n [S] ou [N]: ').upper()
    if alist == 'S':
        print('Meus pesames')
    elif alist == 'N':
        passou == idade - 18
        print(f'{} anos? Você é um anarquista!')




