# Disarium number
def is_disarium(num):
    num_str = str(num)
    return num == sum(int(digit) ** (i + 1) for i, digit in enumerate(num_str))

# Test the function
num = int(input("Enter a number: "))
if is_disarium(num):
    print(f"{num} is a Disarium number.")
else:
    print(f"{num} is not a Disarium number.")

