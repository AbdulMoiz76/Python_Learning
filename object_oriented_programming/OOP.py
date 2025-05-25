# Bsic class and object 
class Car:
    # class Variable 
    total_car = 0


    def __init__(self, brand, model):
# Encapsulation
        self.__brand = brand

        self.__model = model
        Car.total_car += 1


# Getter method
    def get_brand(self):
        return self.__brand + "!!"
    

# Class method self
    def full_name(self):
        return f"{self.__brand} {self.__model} "
    

# Polymorphism    
    def fuel_type(self):
        return "Petrol or Diesel"
    
# Static Method
    @staticmethod
    def general_description():
        return ("Car means of transport.")
    
# Property Dacorator
    @property
    def model(self):
        return (self.__model)
    

#  Inheritance
class ElectricCar(Car):
    def __init__ (self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size


    def full_name(self):
        return f"{self.__brand} {self.__model} with {self.battery_size} battery"
    


# Polymorphism    
    def fuel_type(self):
        return "Electric Car"
    
    
class Battery:
    def battery_info(self):
        return("this is battery")
class Engine:
    def engine_info(self):
        return ("This is Engine.")
class ElectricCar_2(Battery,Engine,Car):
    pass


my_new = ElectricCar_2("teasla","model S")


print(my_new.battery_info())
print(my_new.engine_info())

my_teasla = ElectricCar("teasla","model S", "85kWh")

# print(isinstance(my_teasla,Car))
# print(isinstance(my_teasla, ElectricCar))



# print(my_teasla.fuel_type())
# safari  = Car("Tata", "Safari")
# # safari.model = "city"
# print(safari.model)


# print(Car.total_car)
# print(my_teasla.__brand)
# print(my_teasla.get_brand())





# my_car = Car("Toyota", "Corolla")
# print(my_car.brand)
# print(my_car.full_name())


