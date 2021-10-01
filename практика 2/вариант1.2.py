# №2
import math

x = float(input('Введите x'))
if x >= 0:
    print('y=',math.e ** (math.sqrt(x + math.sqrt(x))))
else:
    print('нет решения')
