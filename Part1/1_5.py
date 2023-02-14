LOWER_1L = 0.10
GREATER_1L = 0.25

bottles1 = int(input('Кол-во бутылок объемом 1л и меньше: '))
bottles2 = int(input('Кол-во бутылок большего объема: '))

res = bottles1 * LOWER_1L + bottles2 * GREATER_1L

print(f'Сумма, которую можно выручить: ${res:.2f}')
