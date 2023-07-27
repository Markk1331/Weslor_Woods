class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def fare(self):
        maintainence_fee = super().fare() *0.1
        return maintainence_fee + super().fare()

School_bus = Bus("School Volvo", 12, 70)
print("Total Bus fare is:", School_bus.fare())
print(type(School_bus))
print(isinstance(School_bus,Vehicle))