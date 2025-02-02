class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def display_info(self):
        return f"Car: {self.brand}, Speed: {self.speed} km/h"

class ElectricCar(Car):
    def __init__(self, brand, speed, battery_capacity):
        super().__init__(brand, speed)
        self.battery_capacity = battery_capacity

    def display_info(self):
        return f"Electric Car: {self.brand}, Speed: {self.speed} km/h, Battery: {self.battery_capacity} kWh"

# Example Usage
car1 = Car("Toyota", 180)
print(car1.display_info())  # Output: Car: Toyota, Speed: 180 km/h

e_car = ElectricCar("Tesla", 200, 75)
print(e_car.display_info())  # Output: Electric Car: Tesla, Speed: 200 km/h, Battery: 75 kWh
