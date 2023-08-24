def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return (a * b) // gcd(a, b)


num1 = int(input("Enter the first positive integer: "))
num2 = int(input("Enter the second positive integer: "))

result = lcm(num1, num2)
print(f"The LCM of {num1} and {num2} is:", result)
