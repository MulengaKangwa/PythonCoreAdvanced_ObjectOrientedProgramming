class Product:
    def __init__(self):
        self.name ="Iphone"
        self.description="It's awesome"
        self.price = 700

    def display(self):
        print(self.name)
        print(self.price)
        print(self.description)

p1 = Product()
p1.display()

p2 = Product()
p2.display()