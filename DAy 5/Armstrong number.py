# Armstrong number
n= int(input("Enter a number:"))
m=n
count= 0
sum1= 0
while(m>0):
    m=m//10
    count= count+1
m=n
while (m>0):
    d= m % 10
    m= m//10
    sum1= sum1+d ** count
if(n==sum1):
    print("number is Armstrong")
else:
    print("number is not Armstrong")
       
