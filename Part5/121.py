import random

nums = []

while (len(nums) < 6):
    n = random.randint(1, 50)
    if n not in nums:
        nums.append(n)

nums.sort()
print(nums)