registro = {'nome': input('Nome: ')}

nasc = int(input('Ano de Nascimento: '))
idade = 2022 - nasc
registro['idade'] = idade
CT = int(input('Carteira de Trabalho (0 não tem): '))
registro['ctps'] = CT
if CT > 0:
    contratacao = int(input('Ano de contratação: '))
    registro['contratação'] = contratacao
    registro['salário'] = float(input('Salário: R$ '))
    aposentadoria = (contratacao - nasc) + 35
    registro['aposentadoria'] = aposentadoria
print('===' * 15)
print(registro)
for k, v in registro.items():
    print(f'{k} é {v}')