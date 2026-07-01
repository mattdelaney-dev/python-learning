def add(*args):
    total = 0
    for n in args:
        total += n

    return total

# print(add(1, 3, 3))

def calculate(**kwargs):

    for key, value in kwargs.items():
        print(key)
        print(value)

class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        
my_car = Car(make="Nissian", model="2008 GTR")
print(my_car.make)