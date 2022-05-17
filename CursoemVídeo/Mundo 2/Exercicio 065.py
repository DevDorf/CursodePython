resp = 's'
cont = soma = 0
while resp in 'Ss':
    num = int(input(f'Digite o valor: '))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num < menor:
            menor = num
        if num > maior:
            maior = num
    resp = (input('Você quer continuar? [N/S]\n')).strip()[0]
media = soma / cont
print(f'Você digitou {cont} valores, sua soma é {soma}, e a média é igual a {media:.1f}')
print(f'O maior valor digitado foi {maior} e o menor {menor}')
