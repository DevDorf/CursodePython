x = int(input())
y = int(input())
cont = y
soma = 0

while cont >= x:
    if cont % 2 == 1:
        soma = cont + soma
    cont = cont + 1
print(soma)

