def find(y):
    max1 = 0
    for i in range(y):
        if y[i] > max1:
            max1 += y
    return max1


input1 = [2, 4, 6, 3, 9, 1]
print(find(input1))
