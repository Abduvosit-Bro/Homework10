class Animal:
    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        print('Bow bow')


class Cat(Animal):
    def make_sound(self):
        print('Meow')


class Cow(Animal):
    def make_sound(self):
        print('Moo')


dog = Dog()
cat = Cat()
cow = Cow()

dog.make_sound()
cat.make_sound()
cow.make_sound()


class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def display_info(self):
        print(self.brand)
        print(self.year)


class Car(Vehicle):
    def __init__(self, brand, year, hp):
        super().__init__(brand, year)
        self.hp = hp

    def display_info(self):
        super().display_info()
        print(self.hp)


class Motorcycle(Vehicle):
    def __init__(self, brand, year, speed):
        super().__init__(brand, year)
        self.speed = speed

    def display_info(self):
        super().display_info()
        print(self.speed)


car = Car('Toyota', 1995, 200)
car.display_info()

motorcycle = Motorcycle('Honda', 2011, 190)
motorcycle.display_info()
