class Counter:
    count = 0
    
    def __init__(self):
        Counter.count +=1
        
    @classmethod
    def display_count(cls):
        return f'total object created:{cls.count}'
    
obj1:Counter = Counter()    
obj1:Counter = Counter()   
obj1:Counter = Counter()   
print(Counter.display_count())