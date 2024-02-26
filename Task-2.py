# 2)Extend the above solution and find the average expense per employee.
# The calculation must be dynamic, there should be no need for you to manually code each addition operations. This can be done by keeping track of the objects being created in a list (But don't manually append the objects to a list, this must happen when the objects are being created).


class Employee:
    all_employees = []

    def __init__(self, name):
        self.name = name
        self.salary = 0
        self.all_employees.append(self)

    def update_salary(self, hours):
        self.salary = hours * 200

class PartTimeEmployee(Employee):
    def update_salary(self, hours):
        self.salary = hours * 150

e1 = Employee(name="Anamika")
e1.update_salary(hours=9)

e2 = Employee(name="Aamy")
e2.update_salary(hours=8)

e3 = PartTimeEmployee(name="Anu")
e3.update_salary(hours=6)

total_expense = sum(emp.salary for emp in Employee.all_employees)
average_expense = total_expense / len(Employee.all_employees) if Employee.all_employees else 0

print("Total Expense:", total_expense)
print("Average Expense per Employee:", average_expense)
