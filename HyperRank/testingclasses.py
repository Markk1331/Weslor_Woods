class Turing:

    def __init__(self, category, year, winner):
        self.category = category
        self.year = year
        self.winner = winner

    def __str__(self):
        return ('{2} was the winner of {0} in {1}'.format(self.category, self.year, self.winner))


# Type your code here.


tu2022 = Turing("Network", 2022, "Robert Metcalfe")

print(tu2022)
