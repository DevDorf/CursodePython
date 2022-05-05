valor_casa = float(input('Qual o valor do imóvel? R$: '))
salario = float(input('Qual o seu salário? R$: '))
anos = int(input('Em quantos anos planeja pagar? '))

prestacao = valor_casa / anos
corte = salario * 30 / 100

if prestacao >= corte:
    print(f'Sinto muito, sua prestação de {prestacao:.2f} exedeu 30%\n', '=== EMPRETIMO NEGADO ===')
else:
    print('=== EMPRESTIMO APROVADO ===')
