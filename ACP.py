#polymorphism-vehicle

class Vehicle:
    def maxSpeed(self):
        pass

class BMW(Vehicle):
    def maxSpeed(self):
        return "BMW max speed is 155 MPH "


class Ferrari(Vehicle):
    def maxSpeed(self):
        return "Ferrari max speed is 249 MPH "

obj = [BMW(), Ferrari()]
for  vehicle in obj:
    print(vehicle.maxSpeed())

