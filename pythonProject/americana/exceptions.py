def check(n,y):
    return list(n + y)

lis1 = [20,45,1,56,1]
lst2 = [5,67,89,2,2]
check1 = check(lis1,lst2)
print(tuple(set(check1)))