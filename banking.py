
class Banking_app:
    def __init__(self, amount):
        self.balance = amount
    def transaction(self, amount):
        with open("bankingfile.txt","a") as file:
             file.write(f"{amount}\t\t\t\tBalance:{self.balance}\n")
    def withdrawal(self,amount):
            try:
                amount = float(amount)

            except ValueError:
            
                amount = 0
            if amount:
                self.balance = self.balance - amount
                self.transaction(f"withdraw: {amount}")
            
        
            
    def deposit(self, amount):
            try:
                amount = float(amount)
            except ValueError:
                amount = 0
            if amount:
                self.balance = self.balance + amount
            self.transaction(f"deposit: {amount}")
            
                 
       

bank = Banking_app(100.00)
        
while True:
    try:
        option = input("what do you want w or d: ")
    except KeyboardInterrupt:
         break
    if option == "w":
        withdraw = input("amount withdraw from the account: ")
        
        bank.withdrawal(withdraw)
        
    elif option == "d":

        add = input("enter the deposit amount: ")
        bank.deposit(add)
       
    else:
            print("please check the option one of the both")
        
    