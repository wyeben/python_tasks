def check_intersection(lst1, lst2):
    elem1 = []
    for elem in lst1:
        elem1.append(elem)
    for elem in lst2:
        elem1.append(elem)
        if elem in lst1 and elem in lst2:
            return elem1


list1 = [1, 2, 3, 4, 5, 6, 7, 1]
list2 = [1, 2, 3, 5, 9, 8, 4]
result = check_intersection(list1, list2)
print(result)
