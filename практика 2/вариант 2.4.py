# №4
import math

x = float(input('Введите x'))
if x >= 0:
    print('y=', math.sqrt(x+ math.sqrt(x+math.sqrt(x))))
else:
    print('нет решения')
