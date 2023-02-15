FIRST = 10.95
OTHER = 2.95

def delivery_cost(items):
    return FIRST + (items-1) * OTHER

items = int(input('Введите кол-во товаров: '))
res = delivery_cost(items)

print(f'Стоимость доставки: ${res:.2f}')