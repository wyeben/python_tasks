def get_copies_of_first_two_chars(s, n):
    if len(s) < 2:
        return s * n
    else:
        first_two_chars = s[:2]
        return first_two_chars * n


input_string = input("Enter a string: ")
num_copies = int(input("Enter the number of copies: "))

result = get_copies_of_first_two_chars(input_string, num_copies)
print("Result:", result)