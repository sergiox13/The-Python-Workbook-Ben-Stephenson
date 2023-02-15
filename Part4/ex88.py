def median(a, b, c):
    return a + b + c - min(a, b, c) - max(a, b, c)


a = int(input('Введите первое значение: '))
b = int(input('Введите второе значение: '))
c = int(input('Введите третье значение: '))

res = median(a, b, c)

print(f'Медиана равна {res}')