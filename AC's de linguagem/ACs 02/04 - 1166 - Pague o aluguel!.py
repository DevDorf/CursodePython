divida = int(input())
mensalidade = int(input())
cont = 1
depois = 0
laco = True
while laco:
    depois = divida - mensalidade
    print(f'pagamento: {cont}')
    print(f'antes = {divida}')
    if depois > 0:
        print(f'depois = {depois}')
    elif depois <= 0:
        depois = 0
        print(f'depois = {depois}')
    print('----')
    cont += 1
    divida = depois
    if depois <= 0:
        laco = False

