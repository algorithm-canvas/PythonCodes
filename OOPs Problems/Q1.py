# Create a car class with attribute like brand and model. Then create an instance of the class

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
            return f"{self.brand} {self.model}"


my_car = Car("Toyota", "Fortuner")
print(my_car.brand)
print(my_car.model)
print(my_car.full_name())

my_new_car = Car("Tata", "Safari")
print(my_new_car.brand)
print(my_new_car.model)
print(my_new_car.full_name())