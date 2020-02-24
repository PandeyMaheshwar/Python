'''print(type([]))
print(type(()))
print(type(200))
print(type(20.5))

class Sample():
    pass

x = Sample()
print(type(x))
'''

class Dog():
    # class object atrribute
    species = "mammal"


    def __init__(self,breed,name): #breed = argument; self = instance ofclass (can use argument)
        self.breed = breed    # __init__ = constructor
        self.name = name
mydog = Dog("lab" ,"ran")
print(mydog.breed)

print(mydog.name)
print(mydog.species)
