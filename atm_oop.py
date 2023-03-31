#parent class
class User():
    def __init__(self,name,age,gender):
        self.name= name
        self.age= age
        self.gender= gender
    def show_detail(self):
        print("Personal Detail") 
        print("")    
        print(f"Name : {self.name}")
        
        print(f"Age : {self.age}") 
        print(f"Gender : {self.gender}") 

#child class

class Bank(User):
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
        self.balance = 0
    def deposit(self,amount):
        self.balance=self.balance + amount 
    def withdrawl(self, amount):
        if amount>self.balance:
            print("insufficient account balance :$", self.balance)
        else:
            print("withdrawl successfull of $",amount) 
            self.balance= self.balance-amount  
            print("Remaining amount is : $",self.balance)  
    def check_balance(self, ):
        print("total balance is $",self.balance )



