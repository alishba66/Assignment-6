from abc import ABC , abstractmethod

class Shape(ABC):
    @abstractmethod
    def area (self):
        pass
    
class Rectangle(Shape):
    def __init__(self, height, width):
        self.height= height
        self.width = width
        
    def area(self):
        return self.height * self.width
    
rect1 :Rectangle= Rectangle (20, 80)
print(f'Area of Rectangle:{rect1.area()}')          