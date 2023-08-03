nums = []
num = input('Enter a num: ')

while num != '':
    nums.append(int(num))
    num = input('Enter a num: ')

avg = sum(nums) / len(nums)
below_avg = []
above_avg = []
equal_avg = []

for num in nums:
    if num < avg:
        below_avg.append(num)
    elif num > avg:
        above_avg.append(num)
    else:
        equal_avg.append(num)

print(f'Numbers below average: {below_avg}.')
print(f'Numbers above average: {above_avg}.')
print(f'Numbers equal to average: {equal_avg}.')