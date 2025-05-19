class Product:
    def __init__(self, price):
        self._price = price  # private attribute

    @property
    def price(self):
        print("Getting price...")
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            print("Price cannot be negative.")
        else:
            print("Setting price...")
            self._price = value

    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price

# Example usage
p = Product(1000)

print(p.price)       
p.price = 1000        
print(p.price)

p.price = -1000   

del p.price          


