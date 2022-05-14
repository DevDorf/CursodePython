def media_aluno(n1, n2, n3, n4):
    return (n1*2 + n2*3 + n3*4 + n4)/10

def aluno_aprovado():
    print('Aluno aprovado.')

def aluno_reprovado():
    print('Aluno reprovado.')

def aluno_exame(media):
    print('Aluno em exame.')
    exame = float(input())
    print(f'Nota do exame: {exame:.1f}')
    media = (media + exame) / 2
    if media >= 5.0:
        aluno_aprovado()
    else:
        print('Aluno reprovado.')
    print(f'Media final: {media:.1f}')

n1, n2, n3, n4 = (input().split())
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

media = media_aluno(n1, n2, n3, n4)
print(f'Media: {media:.1f}')

if media >= 7.0:
    aluno_aprovado()
elif media < 5:
    aluno_reprovado()
else:
    aluno_exame(media)
