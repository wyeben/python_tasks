num_input = input("Enter numbers separated by commas: ")
num_list = num_input.split(',')
num_tuple = tuple(num_list)

print("List:", num_list)
print("Tuple:", num_tuple)