def check(n,t):
    return set([elem for elem in list1 if elem not in list2])


list1 = ["blue", "green", "red", "white"]
list2 = ["blue", "black", "hash", "blue"]
check1 = check(list1,list2)
print(check1)