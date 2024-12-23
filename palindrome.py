input_number = str(input("Enter a string: "))
def palindrome_number(n):
    # Convert the number to a string
    num_str = str(n)
    if num_str == num_str[::-1]:
        print(f"{n} is a palindrome number!")
    else:
        print(f"{n} is not a palindrome number.")


palindrome_number(input_number)
