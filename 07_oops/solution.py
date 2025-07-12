# to make a variable private add underscore before it 2 times
# meaning the class that the variable is in there it can be accessed but 
# if you make a object of the class you won't be be able to access that 
# variable anymore
class Car:
    def __init__(self, brand, model):
        # self gives context, also called this in javascript
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand + " !"

    # this is functionality
    def full_name(self): 
        return f"{self.__brand} {self.model}"


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size


my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
# print(my_tesla.__brand)
print(my_tesla.get_brand())

# my_car = Car("Toyota", "Corolla")
# print(my_car.brand)
# print(my_car.model)
# # this is how you access functionality
# print(my_car.full_name())

# my_new_car = Car("Tata", "Safari")
# print(my_new_car.model)