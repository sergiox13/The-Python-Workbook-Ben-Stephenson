PER_YEAR = 0.04

deposit = int(input('Введите сумму первоначального депозита: '))

total1 = deposit + deposit * PER_YEAR
total2 = deposit + (deposit * PER_YEAR) * 2
total3 = deposit + (deposit * PER_YEAR) * 3

print(f'Сумма на счету после после 1 года: ${total1:.2f}')
print(f'Сумма на счету после после 2 года: ${total2:.2f}')
print(f'Сумма на счету после после 3 года: ${total3:.2f}')
