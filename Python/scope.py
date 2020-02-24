'''x = 25

def my_func():
    x = 50
    return x

print(x)
print(my_func())
print(x)
'''

# Enclosing local function
'''name = "This is a global name!"

def greet():
    name = "Sammy"

    def hello():
        print("hello " +name)

    hello()

greet()
print(name)
'''

# Built-in function

x = 50

def func():
    global x
    x = 1000

print("before function call, x: ",x)
func()
print("after function call, x: ",x)
