def perfect_number(n):
    dividers = []
    for i in range(1, n):
        if n % i == 0:
            dividers.append(i)

    if sum(dividers) == n:
        return True
    return False

print('Perfect Number or not.')
num = int(input('Enter a number: '))
print(perfect_number(num))