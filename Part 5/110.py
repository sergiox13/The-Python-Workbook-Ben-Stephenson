nums = []
n = int(input('Введите число (0 для завершения): '))

while n != 0:
    nums.append(n)
    n = int(input('Введите число (0 для завершения): '))

nums.sort()
print(nums)
