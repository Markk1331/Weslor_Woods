class EV:
    attribute = 'runs on battery'
    attribute2 = "Super car"

    def __init__(self,speed,color):
        self.speed = speed
        self.color = color

    def __str__(self):
        return (f'Your car can travel up to the maximum speed of -- {self.speed}. It {self.attribute}, and the color of choice is {self.color}')

class Taycan(EV):
    def __init__(self,speed, color, price, model ):
        super().__init__(speed,color)
        self.model = model
        self.price = price

    def accleration(speed, distance, model):
        time = distance/(speed/ 3600)/1000
        return (f'{model} accleration time is {time} m/s')

    @classmethod
    def safety(cls,model):
        print(f'{model} will provide maxmium safety to driver on the road')


    def __str__(self):
        return(f'The EV is Model -- {self.model} with {self.color}, the price is {self.price}.')


class Tesla(Taycan):
    def __init(self,speed,color, price, model ):
        super().__init__(speed, color,price,model)

    def maintainence (battery_life):
        repair = (battery_life/24) /365
        print(f'After {repair} years, the trash needs to go for maintainence')


ev = EV(50,'red')
print(ev)

print('\n')

tesla_ev = Tesla(100, "Ugly red", 2000, 'Model 3')
print(tesla_ev)

tesla_acc = Tesla.accleration(100,2000, "Model 3")
print(tesla_acc)

Tesla.maintainence(62000)


print('\n')

Taycan_ev = Taycan(200,"Frozen Blue",500000,'Taycan')
print(Taycan_ev)

taycan_accleration = Taycan.accleration(250,2000, "Taycan")
print(taycan_accleration)
Taycan.safety('Taycan')




