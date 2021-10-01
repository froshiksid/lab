# №1
x = float(input('Введите x'))
y = 1 - x ** 4 - x ** 2
if y >= 0:
    print('y=', 1 / (y ** 0.5))
else:
    print('нет решения')
