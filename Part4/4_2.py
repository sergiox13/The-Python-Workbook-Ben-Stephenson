BASE = 4
EACH = 0.25

def taxi_cost(distance):
    return BASE + (distance//140 * EACH)

distance = int(input('Введите расстояние в м: '))
res = taxi_cost(distance)

print(f'Сумма поездки: ${res:.2f}')