class Bank:
    Bank_name = "State Bank"
    
    @classmethod
    def change_bank_name(cls, name):
        cls.Bank_name = name
       
b1 = Bank()
print(b1.Bank_name)        
Bank.change_bank_name("Mehran Bank")
print(b1.Bank_name)