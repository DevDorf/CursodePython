cont_prod = soma = menor = cont = 0
menor_prod = ' '
print('=-=' * 15)
print('Mercantil Real')
print('=-=' * 15)
while True:
    produto = input('Produto: ')
    preco = float(input('Preço: R$ '))
    cont += 1
    soma += preco
    if cont == 1 or preco < menor:
        menor = preco
        menor_prod = produto
    if preco > 1000:
        cont_prod += 1
    flag = ' '
    while flag not in 'SN':
        flag = input('Você quer continuar? [S/N]').upper().split()[0]
    if flag == 'N':
        print('Volte Sempre')
        break
print('=-=' * 15)
print('Dados da Compra!')
print(f'''
O valor total da compra é R$ {soma:.2f}
Temos {cont_prod} produtos que custam mais do que R$ 1000.00  
O produto {menor_prod} que custa {menor:.2f} é o mais barato da lista''')
