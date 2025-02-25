# Check palendrome number
n=int(input("Enter the value :"))
originalno = n
rev= 0
while (n>0):
    d = n%10
    rev = rev*10 + d
    n= n//10

if originalno ==  rev:
    print("Number is a palindrome")
else:
    print("Number is not palindroime")

