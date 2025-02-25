n = int(input("Enter a number: "))  # Get user input
i = 1
sum1 = 0

while i <= n:
    sum1 = sum1 + i**i  # Add i^i to sum1
    i += 1  # Increment i

print(sum1)  # Print the final result
