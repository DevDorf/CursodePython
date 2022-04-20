import math
a = float(input('Digite um angulo:'))
sen = math.sin(math.radians(a))
cos = math.cos(math.radians(a))
tan = math.tan(math.radians(a))
print('Para o angulo {} temo: \n Seno: {:.2f} \n Cos: {:.2f} \n Tan: {:.2f}'. format(a, sen, cos, tan))
