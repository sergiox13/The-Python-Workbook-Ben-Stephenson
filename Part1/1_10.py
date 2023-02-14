import math

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
print('-' * 25)
message = (
    f'{a}+{b}={a + b}\n'
    f'{a}-{b}={a - b}\n' 
    f'{a}*{b}={a * b}\n' 
    f'{a}/{b}={a / b:.2f}\n' 
    f'{a}%{b}={a % b}\n' 
    f'log10({a})={math.log(a)}\n' 
    f'{a}^{b}={a ** b}'
)

print(message)
          