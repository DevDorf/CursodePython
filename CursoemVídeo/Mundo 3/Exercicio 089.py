alunos = []
soma = cont = 0
while True:
    nome = input('Nome: ')
    nota1 = float(input('Nota1: '))
    nota2 = float(input('Nota2: '))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media])
    resp = input('Deseja continuar? [S/N]: ').strip()
    if resp in 'Nn':
        break
    elif resp not in 'SsNn':
        resp = input('Deseja continuar? [S/N]: ').strip()
print('-=' * 30)
print(f'{"No.":<4}{"Nome":<10}{"Media :>8"}')
print('-' * 25)
for i, a in enumerate(alunos):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-=' * 30)
    resp = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if resp == 999:
        print('Finalizando...')
        break
    if resp <= len(alunos):
        print((f'Notas de {alunos[resp][0]} são {alunos[resp][1]}'))
print('Volte sempre')