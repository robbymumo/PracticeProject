# Description: Design and implement a simple vehicle rental system that allows users to rent different types of
# vehicles, such as cars, motorcycles, and bicycles. The system should support various operations like renting a
# vehicle, returning a vehicle, displaying available vehicles, and calculating rental costs.
#
# Requirements:
#
# 1. Define a base class called Vehicle with common attributes like make, model, year, mileage, and methods like
# display_info(). 2. Create derived classes for different types of vehicles, such as Car, Motorcycle, and Bicycle.
# Each derived class should inherit from the Vehicle base class. 3. Implement specific attributes and methods for
# each derived class. For example, the Car class could have additional attributes like seats and fuel_type,
# whereas the Bicycle class might have an attribute like gears. 4. Implement a class called RentalSystem that manages
# the rental operations. It should have methods like rent_vehicle(), return_vehicle(),
# and display_available_vehicles(). 5. The RentalSystem class should keep track of the rented vehicles,
# available vehicles, and their respective rental costs. 6. Ensure proper error handling, such as preventing renting the
# same vehicle multiple times or returning a vehicle that haven't been rented. 7. Implement appropriate class methods,
# instance methods, and instance variables as needed.

class Vehicle:
    def __init__(self, make, model, year, mileage):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage

    def display_info(self):
        print(f'Vehicle Attributes are:\n'
              f'Make is {self.make}\n'
              f'Model is {self.model}\n'
              f'YOM is {self.year}\n'
              f'Mileage is {self.mileage} Kms')


class Car(Vehicle):
    def __init__(self, seats, fuel_type, make, model, year, mileage):
        super().__init__(make, model, year, mileage)
        self.seats = seats
        self.fuel_type = fuel_type


class Motorcycle(Vehicle):
    def __init__(self, engine_size, top_speed, make, model, year, mileage):
        super().__init__(make, model, year, mileage)
        self.engine_size = engine_size
        self.top_speed = top_speed
        self.is_sportsbike = True

    def toggle_sportsmode(self):
        pass


class Bicycle(Vehicle):
    def __init__(self, frame_material, wheel_size, make, model, year, mileage):
        super().__init__(make, model, year, mileage)
        self.frame_material = frame_material
        self.wheel_size = wheel_size
        self.has_gear = True


class RentalSystem:
    def rent_vehicle(self):
        pass

    def return_vehicle(self):
        pass

    def display_available_vehicles(self):
        pass


vehicle1 = Vehicle('Mazda', 'Atenza', 2023, 1000)

vehicle1.display_info()
