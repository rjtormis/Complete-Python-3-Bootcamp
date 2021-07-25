# Getting familiar with OOP and using Functions and Classes :)
class Dog():
    
    species = 'mammal'

    def __init__(self,breed,name):

        self.breed = breed
        self.name = name
    
    def bark(self,number):
        print(f'Woof! My name is {self.name} and the number is {number}')

my_dog = Dog('Corgi','RTZY')
print(type(my_dog))
print(my_dog.breed)
print(my_dog.name)
my_dog.bark(10)

class Circle():
    
    pi = 3.14

    def __init__(self,radius = 1):
        self.radius = radius
        self.area = radius * radius * Circle.pi
    
    def get_circumference(self):
        return (self.radius * Circle.pi) * 2

my_circle = Circle(30)
print(my_circle.area)
test = my_circle.get_circumference()
print(test)

class Animal():

    def __init__(self):
        print('Animal Created')
    
    def who_am_i(self):
        print('I am an animal')
    
    def eat(self):
        print('I am eating')

print('\n')
class Dog(Animal):
    
    def __init__(self):
        Animal.__init__(self)
        print('Dog Created')
    def bark(self):
        print('Woof! Woof!')

mydog = Dog()
print(mydog.bark())