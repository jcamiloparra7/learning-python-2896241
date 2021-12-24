#
# Example file for working with classes
# LinkedIn Learning Python course by Joe Marini
#

class Vehicle():
    def __init__(self, bodystyle):
        self.bodystyle = bodystyle

        if self.bodystyle == 'Car':
            self.wheels = 4
        elif self.bodystyle == 'Motorcycle':
            self.wheels = 2


class Car(Vehicle):
    def __init__(self, enginetype):
        super().__init__('Car')
        self.enginetype = enginetype

class Motorcycle(Vehicle):
    def __init__(self, enginetype):
        super().__init__('Motorcycle')
        self.enginetype = enginetype

moto1 = Motorcycle('Gasoline')

print(moto1.wheels)
print(moto1.enginetype)
print(moto1.bodystyle)

