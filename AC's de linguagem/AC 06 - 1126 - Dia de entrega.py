dias = ['domingo', 'segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado']
dia_semana = str(input())
diasparaentrega = int(input())

dia_entrega = dias.index(dia_semana) + diasparaentrega

if dia_entrega > 6:
    dia_entrega = dia_entrega - 7

entrega = dias[dia_entrega]

if diasparaentrega == 0:
    print('chega hoje!')
else:
    print('sera entregue {}'.format(entrega))
