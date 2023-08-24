def is_value_in_group(value, group):
    return value in group


group_of_values = [1, 3, 5, 7, 9]

specified_value = int(input("Enter a value to check: "))

if is_value_in_group(specified_value, group_of_values):
    print(f"{specified_value} is in the group of values.")
else:
    print(f"{specified_value} is not in the group of values.")