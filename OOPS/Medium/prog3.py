class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def yearly_salary(self):
        return self.salary * 12

# Example Usage
emp = Employee("Alice", 5000)
print(emp.yearly_salary())  # Output: 60000
