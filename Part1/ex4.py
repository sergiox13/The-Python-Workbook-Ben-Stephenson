length = float(input('Введите длину участка в футах: '))
width = float(input('Введите ширину участка в футах: '))
acres = length * width / 43560
print(f'Площадь садового участка: {acres:.2f} акров')
