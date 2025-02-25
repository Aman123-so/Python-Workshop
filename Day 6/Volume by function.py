#waf to find the volume of sphere , cone, cylinder
r=int(input("radius:"))
h=int(input("height:"))
pi=3.14
def sphere():
    
    volume = (4/3)*pi*r*r*r
    print("volume of sphere",volume)
sphere()
def cone():
    
    volume = (1/3)*pi*r*r*h
    print("volume of cone",volume)
cone()
def cylinder():
    
    volume = pi*r*r*h
    print("volume of cylinder",volume)
cylinder()
