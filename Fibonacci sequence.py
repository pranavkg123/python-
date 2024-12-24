# Function to generate Fibonacci sequence
def fibonacci_sequence(n):
    if n <= 0:
        return "Number of terms must be greater than zero."
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    # Initialize the sequence
    sequence = [0, 1]
    for i in range(2, n):
        next_term = sequence[-1] + sequence[-2]
        sequence.append(next_term)
    
    return sequence

num_terms = int(input("Enter the number of terms: "))
print("Fibonacci sequence:", fibonacci_sequence(num_terms))
