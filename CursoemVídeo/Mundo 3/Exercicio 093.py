ficha = {}
gol = []
totgol = 0
nome = input('Nome do jogador: ')
partidas = int(input(f'Quantas partidas {nome} jogou? '))
ficha['Nome'] = nome
for c in range(1, partidas + 1):
    gols = int(input(f'Quantos gols na {c}ª partida? '))
    totgol += gols
    gol.append(gols)
ficha['gols'] = gol
ficha['total'] = totgol

print('=-=' * 15)
print(ficha)
print('=-=' * 15)
for k, v in ficha.items():
    print(f'{k} é {v}')
print('=-=' * 15)
