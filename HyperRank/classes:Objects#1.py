class Vehicle:
    def __init__(self, name, max_speed,mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

Model_S= Vehicle("Tesla",230,500)
#print(Model_S.max_speed)

bus = Vehicle("School Volvo", 180, 12)
print("Vehicle Name:{}, Speed:{}, Mileage:{}".format(bus.name, bus.max_speed, bus.mileage))


