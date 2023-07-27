class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers."

#bus = Vehicle("bus",0,0)
#bus_cap = bus.seating_capacity(50)

#print(bus_cap)
class Bus(Vehicle):
    def seat_capacity(self, capacity=50):
        return super().seating_capacity(capacity)

School_bus = Bus("School Bus",50,20)

print(School_bus.seating_capacity(50))
