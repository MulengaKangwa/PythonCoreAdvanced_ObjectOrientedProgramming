
# The init method creates an object. Therefore, the object is the assigned a name

class Product:
    def __init__(self):
        self.name ="Iphone"
        self.description="It's awesome"
        self.price = 700

p1 = Product()
print(p1.name)
print(p1.description)
print(p1.price)

p2 = Product()
print(p2.name)
print(p2.description)
print(p2.price)
