

class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.brand = brand
        self.__model = model
        Car.total_car += 1

    def fueltype(self):
        return "Petrol"

    @staticmethod
    def gen_desicription():
        return "Cars are hot n cool at same time"

    @property
    def model(self):
        return self.__model
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fueltype(self):
        return "Electricity"


my_car = ElectricCar("Tesla", "Model X", "85KWH")
print(isinstance(my_car,Car))
print(isinstance(my_car,ElectricCar))
my_car2 = ElectricCar("Tesla", "Model Y", "85KWH")

my_new_car = Car("Tata", "Safari")

print(my_new_car.brand)
print(my_new_car.model)
print(my_new_car.fueltype)

print(my_car.brand)
print(my_car.model)
print(my_car.battery_size)
print(my_car.fueltype())

print(Car.total_car)

print(Car.gen_desicription())
