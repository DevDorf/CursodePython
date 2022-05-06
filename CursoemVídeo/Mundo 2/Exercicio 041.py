ano_nasc = int(input('Qual o ano do nascimento?\n'))
idade = 2022 - ano_nasc

if idade <= 9:
    print('CLASSIFICAÇÃO: Mirim')
elif idade > 9 and idade <= 14:
    print('CLASSIFICAÇÃO: Infantil')
elif idade > 14 and idade <= 19:
    print('CLASSIFICAÇÃO: Junior')
elif idade > 19 and idade <= 20:
    print('CLASSIFICAÇÃO: Senior')
elif idade > 20:
    print('CLASSIFICAÇÃO: Master')
