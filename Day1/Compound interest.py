r=int(input("enter the value of r:"))  # Rate of interest per period
h=int(input("enter the value of h:"))  # Number of time period (e.g= year,month etc.)
p=int(input("enter the value of p:"))  # principal amount 
A= p*(1+(r/100))**   # A= Final amount after interest is applied
ci= A - p  
print("Compound interest is:", ci)
