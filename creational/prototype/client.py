from prototype import Prototype


class Car:
    def __init__(self):
        self.make = "Toyota"
        self.model = "Corolla"
        self.year = "2015"

    def __str__(self):
        return f"{self.make} {self.model} {self.year}"
    

car = Car()

prototype = Prototype()
prototype.register_object("car", car)

car_clone = prototype.clone("car")

print(car)
print(car_clone)