value = input("Enter a number or name: ")

if value.isnumeric():
    number = int(value)
    if number < 0:
        print("Invalid input. Please enter a valid input.")
    else:
        print(number)
else:
    print(value)