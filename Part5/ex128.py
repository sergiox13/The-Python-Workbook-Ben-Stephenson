def countRange(lst, mini, maxi):
    c = 0
    for elem in lst:
        if (elem >= mini) and (elem < maxi):
            c += 1
    return c

data1 = [4, 5, 6, 7, 8 ,9, 10]
min1 = 5
max1 = 10
print(countRange(data1, min1, max1))

data2 = [1.11, 1.22, 2.14, 3.45, 5.34 , 7.92, 8.61, 9.53]
min2 = 2.35
max2 = 8
print(countRange(data2, min2, max2))