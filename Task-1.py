# 1)Create a class Employee with name and salary attributes.
# The salary must be calculated and should be initialized to zero.
# Create a method to calculate the salary by taking the no of hours worked and multiply it by 200.You can give no of hours to the method as an argument.
# Now create a child class Part Time Employee by inheriting the Employee class, and by using method overriding (create salary calculation method in this class also with the same name)
# get the salary of part time employee by multiplying no of hours worked by 150.
# Create 3 objects for each class.
# Now implement'+' operator overloading and find the total salary expense for keeping those employees by adding up the objects together.


class Employee:
    def __init__(self, name):
        self.name = name
        self.salary = 0

    def update_salary(self, hours):
        self.salary = hours * 200

class PartTimeEmployee(Employee):
    def update_salary(self, hours):
        self.salary = hours * 150

def calculate_total_expense(*employees):
    total_expense = sum(emp.salary for emp in employees)
    return total_expense

e1 = Employee(name="Anamika")
e1.update_salary(hours=9)

e2 = Employee(name="Aamy")
e2.update_salary(hours=8)

e3 = PartTimeEmployee(name="Anu")
e3.update_salary(hours=6)

total_expense = calculate_total_expense(e1, e2, e3)
print("Total Expense:", total_expense)
