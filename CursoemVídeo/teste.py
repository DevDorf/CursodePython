'''for c in range(1, 3):
    print(c)
print('Fim')'''

'''c = 1
while c < 10:
    print(c)
    c+= 1
print('Fim')'''

'''r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = input('Você quer continuar? [S/N] ').upper()
print('Fim')'''

n = 1
impar = par = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Vôce digitou {par} numeros pares e {impar} numeros impares!')