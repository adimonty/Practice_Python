def generate_fibonacci(n):
    fibonacci_sequence = [0, 1]
    
    for i in range(2, n):
        next_fibonacci = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_fibonacci)
    
    return fibonacci_sequence

'''User Imput'''
try:
    num_numbers = int(input("Enter the number of Fibonacci numbers to generate: "))
    if num_numbers <= 0:
        print("Please enter a positive integer.")
    else:
        fibonacci_numbers = generate_fibonacci(num_numbers)
        print("Generated Fibonacci numbers:", fibonacci_numbers)
except ValueError:
    print("Please enter a valid integer.")
