n= int(input("Enter a no."))
sum1=0
while n>0 :
    
    d= n%10
    sum1 = sum1+d
    n=n//10
print(sum1)
