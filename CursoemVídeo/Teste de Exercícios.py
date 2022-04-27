A, B, C = map(float, input().split(" "))
tri = (A*C)/2
cir = 3.14159*C**2
tra = ((A + B) * C)/2
qua = B*B
ret = A*B
print('TRIANGULO: {:.3f}'.format(tri))
print('CIRCULO: {:.3f}'.format(cir))
print('TRAPEZIO: {:.3f}'.format(tra))
print('QUADRADO: {:.3f}'.format(qua))
print('RETANGULO: {:.3f}'.format(ret))
