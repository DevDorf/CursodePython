num = int(input('Digite um numero:'))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\33[33m', end=' ') #\33[33m cor amarela
        tot += 1
    else:
        print('\033[31m', end=' ') # \033[31m cor vermelha
    print(f'{c}', end=' ')
print(f'\n\033[mO numero {num} foi divisível {tot} vezes')
if tot == 2:
    print('Por isso ele é PRIMO')
else:
    print('por isso não é primo')
