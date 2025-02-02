class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Example Usage
p1 = Person("Alice", 25)
p1.display()  # Output: Name: Alice, Age: 25
