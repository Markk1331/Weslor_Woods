class Vehicle:
    color = "White"
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass


Audi = Car("Audi",250,500)
Truck = Bus("Scania", 110, 1000)

print(f"Color:{Audi.color}, Vehicle name: {Audi.name}, Vehicle speed:{Audi.max_speed}, Vehicle mileage:{Audi.mileage}")


