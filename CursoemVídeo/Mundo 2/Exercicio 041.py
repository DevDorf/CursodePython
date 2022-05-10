from datetime import date
ano_nasc = int(input('Qual o ano do nascimento?\n'))
idade = date.today().year - ano_nasc

if idade <= 9:
    print('CLASSIFICAÇÃO: Mirim')
elif idade <= 14:
    print('CLASSIFICAÇÃO: Infantil')
elif idade <= 19:
    print('CLASSIFICAÇÃO: Junior')
elif idade <= 20:
    print('CLASSIFICAÇÃO: Senior')
elif idade > 20:
    print('CLASSIFICAÇÃO: Master')
