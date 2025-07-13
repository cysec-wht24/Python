# To make a variable private add underscore before it 2 times
# meaning the class that the variable is in there it can be accessed but 
# if you make a object of the class you won't be be able to access that 
# variable anymore.
# Immediate garbage collection does not happen in python.
# Static method is basically which can only be accessed by a class and 
# not by the instance of the object. when you add @staticmethod you don't ned to use self
# @staticmethod = decorators
# -------------------------------
# CLASS: Car (Base class)
# -------------------------------
class Car:
    # Class variable to keep track of total number of Car instances created
    total_car = 0

    def __init__(self, brand, model):
        # Encapsulated (private) brand attribute using double underscore
        self.__brand = brand
        # Encapsulated model attribute (read-only using @property later)
        self.__model = model
        # Increment class variable whenever a new car is created
        Car.total_car += 1

    # Getter method to access private brand variable (encapsulation)
    def get_brand(self):
        return self.__brand + " !"

    # Instance method using `self` to return full name of the car
    def full_name(self):
        return f"{self.__brand} {self.__model}"

    # Method to demonstrate polymorphism (will be overridden in child class)
    def fuel_type(self):
        return "Petrol or Diesel"

    # Static method: doesn't depend on instance or class variables
    @staticmethod
    def general_description():
        return "Cars are means of transport"

    # Property decorator to make `model` read-only (no setter defined)
    @property
    def model(self):
        return self.__model


# -------------------------------
# CLASS: ElectricCar (Inherits from Car)
# -------------------------------
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        # Call parent constructor using super()
        super().__init__(brand, model)
        # Additional attribute specific to ElectricCar
        self.battery_size = battery_size

    # Override fuel_type method (polymorphism example)
    def fuel_type(self):
        return "Electric charge"


# -------------------------------
# CLASS: Battery (for Multiple Inheritance)
# -------------------------------
class Battery:
    def battery_info(self):
        return "This is battery"

# -------------------------------
# CLASS: Engine (for Multiple Inheritance)
# -------------------------------
class Engine:
    def engine_info(self):
        return "This is engine"

# -------------------------------
# CLASS: ElectricCarTwo (Multiple Inheritance)
# Inherits from Battery, Engine, and Car
# Order matters: Python uses Method Resolution Order (MRO)
# -------------------------------
class ElectricCarTwo(Battery, Engine, Car):
    pass


# -------------------------------
# OBJECT CREATION AND DEMO
# -------------------------------
# Creating object of ElectricCarTwo which inherits from multiple classes
my_new_tesla = ElectricCarTwo("Tesla", "Model S")

# Accessing methods from parent classes (Battery and Engine)
print(my_new_tesla.engine_info())   # Output: This is engine
print(my_new_tesla.battery_info())  # Output: This is battery


# -------------------------------
# Additional Sample Code to Explore
# -------------------------------

# Check isinstance() usage
# my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
# print(isinstance(my_tesla, Car))         # True
# print(isinstance(my_tesla, ElectricCar)) # True

# Try accessing private attribute directly (will raise error)
# print(my_tesla.__brand)  # AttributeError

# Try calling overridden method
# print(my_tesla.fuel_type())  # Electric charge

# Create a car instance
# my_car = Car("Tata", "Safari")

# Try to change read-only property (will raise AttributeError)
# my_car.model = "City"  # AttributeError

# Call static method
# print(Car.general_description())  # Cars are means of transport

# Access property
# print(my_car.model)  # Safari

# Create another car
# my_new_car = Car("Toyota", "Corolla")
# print(my_new_car.full_name())  # Toyota Corolla

# Print total number of cars created
# print(Car.total_car)  # e.g., 3
