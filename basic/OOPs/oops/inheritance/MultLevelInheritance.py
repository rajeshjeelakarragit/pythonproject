class Vehicle:
    def start(self):
        print("Vehicle is starting.")

class Car(Vehicle):
    def start(self):
        print("Car is starting.")

class Bike(Car):
    def start(self):
        print("Bike is starting.")

# Usage
vehicle = Vehicle()
car = Car()

vehicle.start()
car.start()
