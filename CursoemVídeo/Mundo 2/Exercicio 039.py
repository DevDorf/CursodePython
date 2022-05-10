from datetime import date
print('Calculadora de alistamento')
sexo = input('Você é do sexo feminino ou masculino? \n [F] [M]:').upper()
if sexo == 'F':
    print('Você não precisa se alistar, tenha um bom dia!')
elif sexo == 'M':
    ano_nasc = int(input('Em que ano você nasceu? '))
    idade = date.today().year - ano_nasc
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
            passou = idade - 18
            print(f'{passou}  anos se passaram? Você é um anarquista!')




