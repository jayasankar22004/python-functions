class Car:
    wheels = 4
    def __init__(self, mileage):
        self.mileage = mileage
    def display_specs(self):
        print("Mileage:", self.mileage)
        print("Wheels:", self.wheels)
    @classmethod
    def change_wheels(cls, new_wheels):
        cls.wheels = new_wheels
c1 = Car(20)
c1.display_specs()
Car.change_wheels(6)
print("after change:")
c1.display_specs()