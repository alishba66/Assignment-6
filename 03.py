class Car:
    def __init__(self,brand):
        self.brand = brand
    def start (self):
        return f'{self.brand} is starting.' 
    
car = Car("Cultax")
print(car.brand)
print(car.start())    