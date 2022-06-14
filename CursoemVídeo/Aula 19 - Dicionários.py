'''pessoa = {'nome': 'Gustavo', 'Sexo': 'M', 'idade': 22}
print(f'O {pessoa["nome"]} tem {pessoa["idade"]} anos.')
print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())
print('---' * 20)
for k, v in pessoa.items():
    print(f' {k} = {v}')

del pessoa['Sexo'] #deletar uma key
pessoa['peso'] = 98,5 #adicionar uma nova key
pessoa['nome'] = 'Leandro' #substituir o values da key'''


'''brasil = []
estado1 = {'uf': 'rio de janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'são paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil[0]['uf']) #mostra um item especifico do dicionario dentro da lista
'''

estado = {}
brasil = []
for c in range(0, 3):
    estado['uf'] = input('Unidade Federativa: ')
    estado['sigla'] = input('Sigla do Estado: ')
    brasil.append(estado.copy()) #faz a copia do dicionario sem o fatiamento
print(brasil)

for e in brasil:
    for k, v in e.items(): #varre o dicionário e mostra os valores
        print(f'O campo {k} tem valor {v}')