# Name: Xander
# File Name: MO3 Lab- Case Study: Lists, Functions, and Classes .py
# This app will allow the user to input the information of the car and
# will display the information back to the user

# setting up Super Class Vehicle
class Vehicle():
    def __init__(self, car, truck, plane, boat, broomstick):
        self.car = car
        self.truck = truck
        self.plane = plane
        self.boat = boat
        self.broomstick = broomstick

# setting up the Automobile class that inherits Vehicle
class Automobile(Vehicle):
    def __init__(self, car, year, make, model, doors, roof):
        self.car = car
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

# creating the inputs for the information of the car
print ("Please enter your car's information in the inputs below.")
vehicle_type = "car"
year_made = input("What is the year of your car?: ")
car_make = input("What is the make of your car?: ")
car_model = input("What is the model of your car?: ")
door_number = input("Does your car have two or four doors?: ")
roof_type = input ("Does your car have a solid or sun roof?: ")

# Putting the information back into the class
myCar = Automobile(vehicle_type, year_made, car_make, car_model, door_number, roof_type)

#Printing out all of the information in a formatted way
print(f"Vehicle Type: {myCar.car}")
print(f"Year: {myCar.year}")
print(f"Make: {myCar.make}")
print(f"Model: {myCar.model}")
print(f"Number of Doors: {myCar.doors}")
print(f"Type of Roof: {myCar.roof}")
