

"""18. Property Decorators: @property, @setter, and @deleter
Assignment:
Create a class Product with a private attribute _price. Use @property to get the price,
 @price.setter to update it, and @price.deleter to delete it."""

class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        """Get the price."""
        return self._price

    @price.setter
    def price(self, value):
        """Set the price."""
        if value >= 0:
            self._price = value
        else:
           print("Price cannot be negative.")
    @price.deleter
    def price(self):
        """Delete the price."""
        print("Deleting price...")
        del self._price
item = Product(100)
print(item.price)  # Output: 100
item.price = 150
print(item.price)  # Output: 150
item.price = -50  # Output: Price cannot be negative.
del item.price  # Output: Deleting price...