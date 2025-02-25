a= int(input("Enter subject1:"))
b= int(input("Enter subject2:"))
c= int(input("Enter subject3:"))
d= int(input("Enter subject4:"))
e= int(input("Enter subject5:"))
def sub():
    sum =a+b+c+d+e
    print (sum)
sub()
def per():
    per= (a+b+c+d+e)/5
    print(per)
per()
def grade():
    total=(a+b+c+d+e)/5
    if(50<=total<60):
        print("Grade:D")
    elif(60<=total<70):
        print("Grade:C")
    elif(70<=total<80):
        print("Grade:B")    
    elif(80<=total<90):
        print("Grade:A")
    elif(90<=total<100):
        print("Grade:A+")
grade ()      
















        
    
    
