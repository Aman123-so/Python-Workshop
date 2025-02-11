# Question 
#Write a Python program that asks the user to enter their years of experience and current salary. If the experience is 5 years or more, the employee gets a 5% bonus on their salary. The program should then calculate and display the total salary after adding the bonus (if applicable).
x = int(input("Enter your years of experience: "))
y = float(input("Enter your salary: "))

if x >= 5:
    bonus = y * 0.05  # 5% bonus
    total_salary = y + bonus
    print(f"Total salary after 5% bonus: {total_salary}")
else:
    total_salary = y
    print(f"Total salary: {total_salary}")
