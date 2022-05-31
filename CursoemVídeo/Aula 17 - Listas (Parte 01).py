'''num = [2, 5, 9, 1]
num[2] = 3
num.append(7) # adiciona no final da lista

num.sort(reverse = True) #coloca em ordem

num.insert(2, 2) # adiciona um elemento em um indicie indicado

# num.pop(2) #elimina na posição indicada, se não retira no final

num.remove(2) #remove o valor pelo nome dele e não pelo indice

if 5 in num:
    num.remove(5)
print(num)
print(f'Essa lista tem {len(num)}')'''
#----------------------------------------------------------------------
'''valores = []
valores.append(5)
valores.append(9)
valores.append(4)
for cont in range(0, 5):
    valores.append(int(input('Digite um valor')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei {v}')
print(f'Terminei de mostras os valores')'''
#-----------------------------------------------------------------------
a = [2, 3, 8, 7]
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
