# Marks and grade
x= int(input("Enter marks:"))
if 100>= x >=90:
    print("Grade 'A'")
elif 90>= x >= 81:
    print("Grade 'B'")
elif 80>= x >=71:
     print("Grade 'C'")
elif 70>= x >=61:
    print("Grade 'D'")
elif 60>= x >= 51:
    print("Grade 'E'")
elif x>100:
     print("Wrong entry")
else:
    print("Fail")
