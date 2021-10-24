
from os import system
import math

system("clear")

class Bird:

    '''This is a class of birds. This class has provision for storing the
details of various species of birds.'''

    species = "Aves"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method:
    def describe(self):
        return f"{self.name} is {self.age} years old."


class Dog:
    'This is a class of Dogs and really doesn\'t do a lot.'

    def __init__(self, name, age):
        self.age = age
        self.name = name

    def __str__(self):
        return f"{self.name} is {self.age} years old."


bird = Bird("Parrot", 10)

dog = Dog("Tommy", 2)

print(bird)

print(dog)
