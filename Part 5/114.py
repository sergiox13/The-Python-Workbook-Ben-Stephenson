nums = []

num = input('Enter a num: ')

while num != '':
    nums.append(int(num))
    num = input('Enter a num: ')

nums.sort()
print(nums)
