def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


num1 = int(input("Enter the first positive integer: "))
num2 = int(input("Enter the second positive integer: "))

result = gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is:", result)