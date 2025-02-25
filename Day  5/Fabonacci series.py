n = int(input("Enter the number of terms for the Fibonacci series: "))
if n <= 0:
    print("Please enter a positive integer.")
else:
    a, b = 0, 1
    print("Fibonacci Series:")
    for i in range(n):
        print(a , end=" ")
# Update terms
        a, b = b, a + b

