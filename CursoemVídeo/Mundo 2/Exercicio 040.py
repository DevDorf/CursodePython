nota1 = float(input('Qual Nota 1?\n '))
nota2 = float(input('Qual Nota 2?\n '))
media = (nota1 + nota2)/2

if media >= 7:
    print(f'Parabens, sua média foi de: {media:.2f}')
elif media < 7 and media >= 5:
    print(f'Você esta em recuperação, sua média é: {media:.2f}')
else:
    print(f'Você foi reprovado, sua media foi: {media:.2f}')