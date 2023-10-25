def find(y):
    max1 = 0
    for i, r in range(y):
        if y[i] > y[r]:
            max1 += y
    return max1


input1 = [2, 4, 6, 3, 9, 1]
print(find(input1))
