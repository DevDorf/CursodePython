escola = []
alunos = []
notas = []
soma = media = cont = 0
while True:
    nome = input('Nome: ')
    nota1 = float(input('Nota1: '))
    nota2 = float(input('Nota2: '))
    alunos.append(nome)
    notas.append(nota1)
    notas.append(nota2)
    alunos.append(notas[:])
    escola.append(alunos[:])
    notas.clear()
    alunos.clear()
    resp = input('Deseja continuar? [S/N]: ').strip()
    if resp in 'Nn':
        break
    elif resp not in 'SsNn':
        resp = input('Deseja continuar? [S/N]: ').strip()

# fazer calculo da média das notas

print('-=-=' * 20)
print(f'No. NOME        MEDIA')
print('---' * 20)



print(escola)
