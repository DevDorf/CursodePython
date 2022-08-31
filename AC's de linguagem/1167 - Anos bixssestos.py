def ano_bissesto(inicio):
    return inicio % 4 == 0 and inicio % 100 != 0 or inicio % 400 == 0

inicio = int(input())
fim = int(input())
biss = 0
while inicio < fim + 1:
    if ano_bissesto(inicio):
        print(inicio)
        biss += 1
    inicio += 1
print(f'bissextos: {biss}')

'''Primeira situação: Se o ano de 2015 ou 2016 for uma divisão exata em relação a 4,
 deveremos verificar, em seguida, se não é divisível por 100. Se não for, o ano será bissexto;

Segunda situação: Se o ano  não for divisível por 4,
então deveremos verificar se ele é divisível por 400. Se também não for divisível,
 o ano de 2015 não será bissexto;

Terceira situação: Se o ano de 2015 ou 2016 não for divisível por 4,
 então devemos verificar se ele é divisível por 400. Caso seja, o ano de 2015 é bissexto.
'''