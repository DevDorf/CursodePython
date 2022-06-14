alunos = {'Nome': input('Nome do aluno: '), 'Media': int(input('Média do aluno: '))}

if alunos['Media'] >= 7:
    alunos['Situação'] = 'Aprovado'
else:
    alunos['Situação'] = 'Reprovado'
for k, v in alunos.items():
    print(f'{k} é igual a {v}')
