def moving_zeros(t):
    count_zeros = t.count(0)
    t = [x for x in t if x != 0]
    t.extend([0] * count_zeros)
    return t


array = [4, 3, 0, 2, 0, 4, 10, 12]
print(moving_zeros(array))
