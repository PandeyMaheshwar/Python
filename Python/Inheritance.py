# INHERITANCE
class Animal():

    def __init__(self):
        print("Animal Created")

    def whoAmI(self):
        print("Animal")

    def eat(self):
        print("Eating")

class dog(Animal):
    def __init__(self):
        #Animal.__init__(self)
        print("Dog created")

    def bark(self):
        print("woof")

mya = dog()
mya.whoAmI()
mya.eat()
mya.bark()
