class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def save_to_file(self, filename):
        with open(filename, "w") as file:
            file.write(f"{self.length},{self.width}")

    @staticmethod
    def read_from_file(filename):
        with open(filename, "r") as file:
            data = file.read().strip().split(",")
            return Rectangle(float(data[0]), float(data[1]))

# Example Usage
rect = Rectangle(5, 3)
rect.save_to_file("rectangle.txt")

loaded_rect = Rectangle.read_from_file("rectangle.txt")
print(loaded_rect.length, loaded_rect.width)  # Output: 5.0 3.0
