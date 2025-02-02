class Vehicle:
    def __init__(self, plate, vehicle_type):
        self.plate = plate
        self.vehicle_type = vehicle_type

class ParkingLot:
    def __init__(self, capacity):
        self.capacity = capacity
        self.parked_vehicles = {}

    def park_vehicle(self, vehicle):
        if len(self.parked_vehicles) < self.capacity:
            self.parked_vehicles[vehicle.plate] = vehicle
            return f"Vehicle {vehicle.plate} parked."
        return "Parking Lot Full!"

    def remove_vehicle(self, plate):
        if plate in self.parked_vehicles:
            del self.parked_vehicles[plate]
            return f"Vehicle {plate} removed."
        return "Vehicle not found."

# Example Usage
lot = ParkingLot(2)
car1 = Vehicle("ABC123", "Car")
bike1 = Vehicle("XYZ789", "Bike")

print(lot.park_vehicle(car1))  # Output: Vehicle ABC123 parked.
print(lot.park_vehicle(bike1))  # Output: Vehicle XYZ789 parked.
print(lot.remove_vehicle("ABC123"))  # Output: Vehicle ABC123 removed.
