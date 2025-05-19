class Dog():
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        
    def bark(self):
        return f'{self.name} says woofff!'
    
dog = Dog("Tommy" , "Labrador")  
print(dog.bark())      
    