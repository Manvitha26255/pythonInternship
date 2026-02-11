class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def __eq__(self, other):
        if isinstance(other, Mobile):
            return self.brand == other.brand and self.model == other.model
        return False

mobile1 = Mobile("Apple", "iPhone 15", 80000)
mobile2 = Mobile("Apple", "iPhone 15", 75000)
mobile3 = Mobile("Samsung", "S23", 70000)

print(mobile1 == mobile2)  
print(mobile1 == mobile3)  
print(mobile2 == mobile3)  
