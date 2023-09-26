def find_second_largest_digit(input_string):
    digits = [char for char in input_string if char.isdigit()]
    if len(digits) < 2:
        return -1

    digits.sort(reverse=True)
    return digits[1]


input_string = "abc1111"
second_largest_digit = find_second_largest_digit(input_string)

if second_largest_digit != -1:
    print(f"The second largest digit is: {second_largest_digit}")
else:
    print("There are not enough digits to determine a second largest digit.")
