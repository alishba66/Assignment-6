class Student():
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    def display(self):
        return(f"Name:{self.name}\nMarks:{self.marks}")
        
s1 = Student("Ali" , 58)    
print(s1.display())
     
        
     