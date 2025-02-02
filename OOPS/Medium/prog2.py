class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def average_grade(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0

# Example Usage
s1 = Student("John", 101)
s1.add_grade(85)
s1.add_grade(90)
s1.add_grade(78)
print(s1.average_grade())  # Output: 84.33
