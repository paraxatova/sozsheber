class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def save_to_file(self):
        with open("employee.txt", "w") as f:
            f.write(f"{self.name} - {self.salary}")

# Tuwri sheshim (SRP tiykarinda)
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class EmployeeSaver:
    def save_to_file(self, employee):
        with open("employee.txt", "w") as f:
            f.write(f"{employee.name} - {employee.salary}")

# Paydalaniwshi
emp = Employee("Ali", 5000)
saver = EmployeeSaver()
saver.save_to_file(emp)
