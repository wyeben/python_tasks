def split_list(input, size):
    return [input[i:: size] for i in range(size)]


input = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
size = 3

change = split_list(input, size)
print(change)
