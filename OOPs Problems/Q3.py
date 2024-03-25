# Modify the car class to encapsulate the brand attribute, making it private and provide a getter method for it

class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand + " !"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size


my_car = ElectricCar("Tesla", "Model X", "85KWH")
print(my_car.__brand)
print(my_car.model)
print(my_car.battery_size)
print(my_car.get_brand())