def isSorted(lst):

    temp1 = lst.copy()
    temp2 = lst.copy()
    temp1.sort()
    temp2.sort(reverse=True)

    if lst == temp1 or lst == temp2:
        return True
    return False

lst = []

num = int(input('Enter length of list: '))

for i in range(num):
    lst.append(int(input('Enter a number: ')))

print(f'List sorted? {isSorted(lst)}')