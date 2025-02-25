def is_armstrong(n):
    m = n  
    count = len(str(n))  
    sum1 = 0  

    while m > 0:
        d = m % 10
        sum1 += d ** count
        m //= 10

    # Check if the number is Armstrong
    if n == sum1:
        print("Number is Armstrong")
    else:
        print("Number is not Armstrong")

# Taking input
n = int(input("Enter a number: "))
is_armstrong(n)
