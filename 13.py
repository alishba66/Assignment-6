class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self, engine: Engine):
        self.engine = engine  

    def start_car(self):
        return self.engine.start() 


engine1 = Engine()
car1 = Car(engine1)

print(car1.start_car())  
