TIPS = 0.18
TAX = 0.12

check = float(input('Введите сумму чека: '))

tax_sum = check * TAX
tips_sum = check * TIPS
check_sum = check + tax_sum +tips_sum

print(f'Налог: ${tax_sum}')
print(f'Сумма чаевых: ${tips_sum}')
print(f'Итоговая сумма: ${check_sum}')
