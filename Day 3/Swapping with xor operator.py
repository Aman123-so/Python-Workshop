# Function to swap two variables using XOR
def swap_using_xor(a, b):
    
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b
a= int (input("Enter a value of a:"))
b= int (input("Enter a value of b:"))
print("Before swapping:")
print("x =", a)
print("y =", b)
x, y = swap_using_xor(a, b)
print("After swapping:")
print("x =", b)
print("y =", a)
