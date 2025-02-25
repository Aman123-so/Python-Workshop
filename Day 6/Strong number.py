import math

# Function to check if a number is a strong number
def is_strong(num):
    total = 0  # Initialize a variable to store the sum of the factorials
    
    # Convert the number into a string to loop through each digit
    for digit in str(num):
        total += math.factorial(int(digit))  # Add the factorial of each digit to the total
    
    # Check if the sum of the factorials equals the original number
    return total == num

# Take user input
num1 = int(input("Enter a number: "))

# Check and print the result
print(f"Is {num1} a strong number? {'Yes' if is_strong(num1) else 'No'}")



