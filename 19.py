class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return self.factor * value

triple = Multiplier(3)


print(callable(triple))


print(triple(20))        
print(triple(10))      
