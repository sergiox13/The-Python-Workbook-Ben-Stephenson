def hypot(a, b):
    return a**2 + b**2

a = int(input('Введите сторону а: '))
b = int(input('Введите сторону b: '))

print(f'Гипотенуза: {hypot(a, b)}')