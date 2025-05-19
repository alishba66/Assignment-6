class Logger():
    def __init__(self):
        print("Logger object is created.")
        
    def __del__(self): 
        print("Logger object is destroyed.")   
        
        
log= Logger()
print(log)        
    
    