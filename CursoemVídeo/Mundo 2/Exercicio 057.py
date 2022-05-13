r = input('Qual seu sexo? [M/F]: ').upper()
while 'F' != r != 'M':
    print('Valor desconhecido, tente novamente')
    print('=-' * 20)
    r = input('Qual seu sexo? [M/F]: ').upper()
if r == 'M':
    print('Bem Vindo')
else:
    print('Bem Vinda')