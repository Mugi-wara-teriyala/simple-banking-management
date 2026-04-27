import time

def main():
    print("Welcome to the bank!")
    kvb = bank("KVB")
    choice = int(input("select option:\n    1) new customer\n    2)existing customer\n"))

    if choice == 1:
        
    
        name = input("Enter name: ")
        acc_no = input("Enter account number: ")
        pin = input("Create a new 4-digit pin: ")
        balance = float(input("Enter the cash you like to deposit: "))
        
        branch = input("Enter branch name: ")
        cos1 = customer(acc_no, name, balance, branch, pin)
        kvb.add_cus(cos1)
        cos1.show_details() 

    elif choice ==2:
        x,attempts = 0,3
        while x!=1 and attempts > 0:
            name = input("enter name:  ")
            
            pin = input("enter pin:  ")
            for i in kvb.customers.values():

                if i.check_c(pin, name):
                    x+=1
                    break
                else:
                    print("customer not found, please try again...")
                    attempts -= 1
                    print(f"{attempts} attempts left")
        if x==1:
            time.sleep(0.75)
            print("\nlogin successful!\n")
            while True:
                time.sleep(0.5)
                try:
                    choice = int(input("\nselect option:\n    1) deposit\n    2)withdraw\n    3)check account details\n    4)change pin\n    5)transaction history\n    6)exit\n"))
                except ValueError:
                    print("Please enter a valid number for the menu choice.")
                    continue

                if choice == 1:
                    amount = float(input("enter the amount you like to deposit: "))
                    i.deposit(amount)
                    time.sleep(0.5)
                    print("amount deposited successfully!")
                elif choice == 2:
                    amount = float(input("enter the amount you like to withdraw: "))
                    time.sleep(0.5)
                    i.withdraw(amount)
                elif choice == 3:
                    time.sleep(0.5)
                    i.show_details()
                elif choice == 4:
                    new_pin = input("create a new 4-digit pin:  ")
                    i.pin = new_pin
                    time.sleep(0.5)
                    print("pin changed successfully!")
                elif choice == 5:
                    time.sleep(0.5)
                    i.show_transaction_history()
                elif choice == 6:
                    time.sleep(0.5)
                    print("thank you for banking with us!")
                    break
                else:
                    print("invalid option, please try again.")
                    
class customer():
    
    def __init__(self,acc_no, name, balance, branch, pin):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance
        self.branch = branch
        self.pin = pin
        self.transaction_hist = []
        for ifsc, name in bank.branch.items():
            if self.branch == name:
                self.ifsc = ifsc
                break
    
    def deposit(self, amount):
            self.balance += amount

            self.transaction_hist.append(("deposit", amount))

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transaction_hist.append(("withdraw", amount))
        else:
            print("Insufficient balance")

    
    def check_c(self, pin, name):
        
        if self.pin == pin and self.name == name:
            return True
        
        return False

    def show_details(self):
        print(f"\nAccount Number: {self.acc_no}")
        print(f"Name    : {self.name}")
        print(f"Branch  : {self.branch}")
        print(f"IFSC    : {self.ifsc}")
        print(f"Balance : ₹{self.balance:.2f}")

    def show_transaction_history(self):
        print("\nTransaction History:")
        for i in self.transaction_hist:
            print(f"{i[0].capitalize()} : ₹{i[1]:.2f}")

class bank():
    branch = {"IFSC001": "KVB Main Branch", "IFSC002": "KVB City Branch", "IFSC003": "KVB Sub Branch"}
    def __init__(self, b_name):
        self.b_name = b_name
        self.balance = 0
        self.customers = {123456: customer(123456, "Alice", 1000, "KVB Main Branch", "1234"),
                          123457: customer(123457, "Bob", 500, "KVB City Branch", "5678")}
        
        # self.transaction_his = []
        self.num_customers = len(self.customers)

    def add_cus(self , customer):
        self.customers[customer.acc_no] = customer
    # def deposit(self, acc_no, amount):
    #     for i in self.customers.values():
    #         if i.acc_no == acc_no:
    #             i.deposit(amount)
    #             # i.transaction_his.append(("deposit", amount))
    #             break
    # def withdraw(self, acc_no, amount):
    #     for i in self.customers.values():
    #         if i.acc_no == acc_no:
    #             i.withdraw(amount)
    #             # i.transaction_his.append(("withdraw", amount))
    #             break

    def check_c(self, pin, name):
        
        if self.pin == pin and self.name == name:
            return True
        
        return False
        
    #def transaction_history(self):
        # print("\nTransaction History:")
        # for i in i.transaction_his:
        #     print(f"{i[0].capitalize()} : ₹{i[1]:.2f}")
        d
    











if __name__ =="__main__":
    main()