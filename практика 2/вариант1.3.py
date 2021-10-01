# №3
x = float(input('Введите x'))
y = float(3 * (x ** 2 - 1))
if y == 0:
    print('y=', (x ** 2 - 1) * (1 - x))
else:
    print('y=', ((x ** 2 + 1) / y) + ((x ** 2 - 1) * (1 - x)))
