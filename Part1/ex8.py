SOUVENIR_W = 75
BAUBLE_W = 112

souvs = int(input('Введите кол-во сувениров: '))
baubles = int(input('Введите кол-во безделушек: '))

total = (souvs * SOUVENIR_W + baubles * BAUBLE_W) / 1000

print(f'Общий вес посылки: {total:.3f} кг.')