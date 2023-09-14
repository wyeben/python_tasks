def create_tuple(l1, l2):
    return list(zip(l1 , l2))


list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10, 11]
check = create_tuple(list1, list2)
print(check)
