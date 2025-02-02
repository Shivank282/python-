class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# Example Usage
rect = Rectangle(5, 3)
print(rect.area())       # Output: 15
print(rect.perimeter())  # Output: 16
