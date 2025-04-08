class Engine:
    def start(self):
        print("Engine started.")

class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        print("Car is starting.")
        self.engine.start()

# Usage
car = Car()
car.start()
