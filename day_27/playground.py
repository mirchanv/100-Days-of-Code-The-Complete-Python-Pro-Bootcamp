# *args - Many/Unlimited Positional Arguments
# args is of type tuple
# The * packs all the arguments into a tuple

def add(*args):
    total_sum = 0
    for num in args:
        total_sum += num
    return total_sum

print(add(1, 2, 3))
print(add(101, 220))
print(add(10, 30, 40, 5, 100))

# **kwargs - Many/Unlimited Keyword Arguments
# kwargs is of type dictionary
# The ** creates a dict of key-value pairs where the keyword arg is the key and the value is the value assigned to it

def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print("n =", n)

calculate(2, add=3, multiply=5)

class Car:

    def __init__(self, **kwargs):
        self.make = kwargs.get("make", "Toyota")
        self.model = kwargs.get("model", "Corolla")
        self.color = kwargs.get("color", "Silver")
        self.max_speed = kwargs.get("max_speed", 180)

my_car = Car(make="BMW", model="M5 Sports Performance")
print(my_car.make, my_car.model)

new_car = Car()
print(new_car.make, new_car.model)