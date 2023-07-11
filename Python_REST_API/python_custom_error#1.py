class Taycan:
    def __init__(self, type_of_road, distance_to_travel):
        self.type_of_road = type_of_road
        self.distance_to_travel = distance_to_travel
        self.battery_remaining = 0


    def battery_drain(self, current_status:int):
        electric_consumption = self.distance_to_travel/ 20
        self.battery_remaining = current_status - electric_consumption

        if self.battery_remaining < 0:
            raise BatteryError('Your car cannot drive below 0% of battery level. Park your car immendiately')
        else:
            return (self.battery_remaining)


    def __str__(self):
        return(f' After traveling {self.distance_to_travel} on the {self.type_of_road}, there will be {self.battery_remaining}% left')

def BatteryError(ValueError):
    pass


taycan = Taycan('Highway', 1100)
taycan.battery_drain(50)
print(taycan)
