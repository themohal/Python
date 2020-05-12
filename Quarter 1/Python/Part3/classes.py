class Car():
    def __init__(self,make,model,year):
        self.make= make
        self.model = model
        self.year =year
    def describe(self):
        print(f"car make is:{self.make}\ncar model is:{self.model}\ncar year is:{self.year}")
    def move(self):
        print("Car has moved...")
    def applyBreak(self):
        print("Car has stopped")
    

car1 = Car("Suzuki","VXR","1992")
car1.describe()
print(car1.make,car1.model,car1.year)

