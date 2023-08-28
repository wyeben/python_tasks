def fibonacci_list_comprehension(limit):
    fib_sequence = [0, 1]
    [fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
     for _ in range(limit) if fib_sequence[-1] + fib_sequence[-2] <= limit]
    return fib_sequence


limit = 50
fibonacci_sequence = fibonacci_list_comprehension(limit)
print(f"Fibonacci series up to {limit}:")
print(fibonacci_sequence)
