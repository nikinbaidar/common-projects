from os import system

system("clear")


class Automobile:
    '''Automobile class with max_speed and mileage instance attributes.'''

    def __init__(self, max_speed, milegae):
        self.max_speed = max_speed
        self.milegae = milegae

    def __str__(self):
        return f"Max speed is {self.max_speed} and Mileage is {self.milegae}."

car = Automobile(280, 18)

print(car)
