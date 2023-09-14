def sum_list(list1, value):
    num_indices = {}

    for i, num in enumerate(list1):
        numb = value - num

        if numb in num_indices:
            return [num_indices[numb], i]

        num_indices[num] = i

    return []


numbers = [5, 4, 9, 7, 2, 0]
value = 16
result = sum_list(numbers, value)
print(result)
