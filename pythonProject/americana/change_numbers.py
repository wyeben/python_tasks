def change_numbers(t, y):
    num = []

    def change(r):
        for char in r:
            if char == 0:
                num.copy()
            else:
                num.append(char)
        return num

    result = change(t)
    result = change(y)
    return result


num1 = [8, 6, 4, 9, 2, 0]
num2 = [4, 5, 0, 2, 3, 6]
print(change_numbers(num1, num2))
