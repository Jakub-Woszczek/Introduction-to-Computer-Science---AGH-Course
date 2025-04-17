class Car:
    def __init__(self,brand):
        self.brand = brand

    def info(self):
        print("Brand:",self.brand)

first_car = Car('Opel')
second_car = Car("skoda")

first_car.info()

class Person:
    def __init__(self,age,weight,height,first_name,Last_name):
        self.age = age
        self.weight = weight
        self.height = height
        self.first_name = first_name
        self.last_name = Last_name

    def walk(self):
        print("Walking...")

    def sleep(self):
        print("Sleeping...")


user = Person(18,73,183,"Jakub","The Vitcher")

print(user.age)
user.walk()

