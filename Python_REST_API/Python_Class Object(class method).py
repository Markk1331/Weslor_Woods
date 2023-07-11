

class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({
            'name': name,
            'price': price
        })

    def stock_price(self):
        total = 0
        for item in self.items:
            total += item['price']
        return total

    @classmethod
    def franchise(cls, store):
        # Return another store, with the same name as the argument's name, plus " - franchise"
        return store.name + ' - franchise'
        #stores = ' - franchise'
        #return store + stores


    @staticmethod
    def store_details(store):

        return('{}, total stock price: {}'.format(store.name, int(store.stock_price())))
        # Return a string representing the argument
        # It should be in the format 'NAME, total stock price: TOTAL'

store = Store('abc')
store.name = 'abc'
store1 = Store('Amazon')
store.add_item('keyboard',52)
franchise_name = store.franchise(store)

#How to process franchise method outcome into store details?

print(store1.name)
print(store.franchise(store))
print(store.store_details(store))
