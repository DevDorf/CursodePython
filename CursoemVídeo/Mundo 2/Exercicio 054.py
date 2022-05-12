from datetime import date
atual = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    ano = int(input(f'Digite o {c}° anos de nascimento: '))
    if atual - ano >= 21:
        maior += 1
    elif atual - ano < 21:
        menor += 1
print(f'{menor} pessoas ainda são menores de idade')
print(f'{maior} pessoas já alcansaram a maior idade')