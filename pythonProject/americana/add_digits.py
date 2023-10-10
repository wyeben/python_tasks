def add_digits(num):
    while num >= 10:
        sum1 = 0
        while num > 0:
            sum1 += num % 10
            num //= 10
        num = sum1
    return num


number = 38
check = add_digits(number)
print(check)
