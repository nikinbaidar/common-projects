from os import system

system("clear")


class Automobile:
    '''Automobile class with max_speed and mileage instance attributes.'''

    capacity = 2

    def __init__(self, name, max_speed, milegae):
        self.name = name
        self.max_speed = max_speed
        self.milegae = milegae

    def __str__(self):
        return f"Automobile name: {self.name} Max speed: {self.max_speed} and Mileage: {self.milegae}."

    @property
    def seating_capacity(self):
        return f"The seating capacity of {self.name}: {self.capacity}"


class Car(Automobile):
    capacity = 4

car1 = Car("Volvo", 180, 20)

print(car1.seating_capacity)
