def divider(n):
    lst = []
    for i in range(1, n):
        if n % i == 0:
            lst.append(i)
    return lst

num = int(input('Введите число: '))
print(divider(num))