# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# super class / parent class (vehicle):
class Vehicle:
    pass
# sub class / child class
class FlightVehicle(Vehicle):
    pass
# sub class / child class
class Starship(FlightVehicle):
    pass
# sub class / child class
class Airplane(FlightVehicle):
    pass
# sub class / child class
class GroundVehicle(Vehicle):
    pass
# sub class / child class
class Car(GroundVehicle):
    pass
# sub class / child class
class Motorcycle(GroundVehicle):
    pass