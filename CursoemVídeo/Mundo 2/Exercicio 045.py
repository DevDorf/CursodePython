from random import randint
print('JOKENPÔ')
print('==='*10)
print('Faça a Sua Escolha:')
print('Pedra')
print('Papel')
print('Tesoura')
print('==='*10)
jogador = input().upper()

computador = randint('PEDRA', 'PAPEL', 'TESOURA')

if computador == 'PEDRA' and jogador == 'PAPEL' :
    print(f'Computador: {computador}\n Jogador: {jogador} \n Jogador VENCEU!!!')
elif computador == 'PEDRA' and jogador == 'TESOURA':
    print(f'Computador: {computador}\n Jogador: {jogador} \n Computador VENCEU!!!')
elif computador == 'PEDRA' and jogador == 'PEDRA':
    print(f'Computador: {computador} \n Jogador: {jogador} \n EMPATE')
elif computador == 'PAPEL' and jogador == 'PEDRA':
    print(f'Computador: {computador} \n Jogador: {jogador} \n Computador VENCEU!!!')
elif computador == 'PAPEL' and jogador == 'TESOURA':
    print(f'Computador: {computador} \n Jogador: {jogador} \n Jogador VENCEU!!!')
elif computador == 'PAPEL' and jogador == 'PAPEL':
    print(f'Computador: {computador} \n Jogador: {jogador} \n EMPATE')
elif computador == 'TESOURA' and jogador == 'PAPEL':
    print(f'Computador: {computador} \n Jogador: {jogador} \n Computador VENCEU!!!')
elif computador == 'TESOURA' and jogador == 'PEDRA':
    print(f'Computador: {computador} \n Jogador: {jogador} \n Jogador VENCEU!!!')
elif computador == 'TESOURA' and jogador == 'TESOURA':
    print(f'Computador: {computador} \n Jogador: {jogador} \n EMPATE')
else:
    print('Valor não reconhecido')



