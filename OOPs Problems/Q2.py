# Create an ElectricCar class that inherits from the Car class and has an additional attribut battery_size

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size


my_car = ElectricCar("Tesla", "Model X", "85KWH")
print(my_car.brand)
print(my_car.model)
print(my_car.battery_size)
