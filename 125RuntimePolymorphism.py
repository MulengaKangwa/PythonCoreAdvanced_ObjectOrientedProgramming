# This is the first video on inheritance.

class BMW:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year

    def start(self):
        print("Starting the car")
    def stop(self):
        print("Stopping the car")


class ThreeSeries(BMW):
    def __init__(self,cruiseControlEnabled,make,model,year):
        super().__init__(make,model,year)
        self.cruiseControlEnabled =cruiseControlEnabled
    def display(self):
        print(self.cruiseControlEnabled)
    def start(self):
        print("Button Start") # This is overriding.

class FiveSeries(BMW):
    def __int__(self,parkingAssistantEnabled,make,model,year):
        super.__init__(make,model,year)
        self.parkingAssistantEnabled = parkingAssistantEnabled

bmw=ThreeSeries(True,"BMW","328i","2018") #Instead of writing ThreeSeries, you can write bmw due to polymorphism
print(bmw.cruiseControlEnabled)
print(bmw.make)
print(bmw.model)
print(bmw.year)

bmw.start()
bmw.stop()
bmw.display()

# This is the missing the entries for the FiveSeries