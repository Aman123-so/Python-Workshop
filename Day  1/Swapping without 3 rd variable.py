# Swapping two number without 3rd variable
a= int(input("Enter a :"))
b= int(input("Enter b :"))
print("before swapping :", (a,b))
a = a+b
b = a-b
a= a-b
print("After Swapping:" ,(a,b))
