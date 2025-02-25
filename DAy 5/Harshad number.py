# Harshad number (A Harshad number is a number that is divisible by the sum of its digits.)
def is_harshad(num):
    return num % sum(int(digit) for digit in str(num)) == 0

# Test the function
num = int(input("Enter a number: "))
if is_harshad(num):
    print(f"{num} is a Harshad number.")
else:
    print(f"{num} is not a Harshad number.")

