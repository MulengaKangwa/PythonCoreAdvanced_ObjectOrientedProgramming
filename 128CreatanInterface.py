# This is the first video on inheritance.

from abc import abstractmethod,ABC
class BMW(ABC):
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year

    @abstractmethod  # Step 1: This makes it an abstract method but it is not implemented
    def drive(self):
        pass

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class ThreeSeries(BMW):
    def __init__(self,cruiseControlEnabled,make,model,year):
        super().__init__(make,model,year)
        self.cruiseControlEnabled =cruiseControlEnabled

    def display(self):
        print(self.cruiseControlEnabled)

    def start(self):
        super().start()
        print("Button Start")

    def stop(self):
        super().stop()
        print("Button Stop")

    def drive(self):
        print("Three Series is being driven.")

class FiveSeries(BMW):
    def __int__(self,parkingAssistantEnabled,make,model,year):
        super.__init__(make,model,year) # By substituting BMW with Super(), the self is not needed.
        self.parkingAssistantEnabled = parkingAssistantEnabled

    def display(self):
        print(self.parkingAssistantEnabled)

    def start(self):
        super().start()
        print("Remote Start")

    def stop(self):
        super().stop()
        print("Remorte Stop")

    def drive(self):
        print("Five Series is being driven.")

threeSeries=ThreeSeries(True,"BMW","328i","2018")
print(threeSeries.cruiseControlEnabled)
print(threeSeries.make)
print(threeSeries.model)
print(threeSeries.year)

threeSeries.start()
threeSeries.stop()
threeSeries.display()

# This is the missing the entries for the FiveSeries
