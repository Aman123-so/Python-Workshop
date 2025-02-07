x=[24,42.42, "Ram", 4+3j,43]
##temp= x[0]
##x[0]= x[-1]
##x[-1]= temp
temp=x[1]
x[1]= x[3]
x[3]=temp
print(x)

