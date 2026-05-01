import time
from datetime import datetime
import sqlite3
from tabulate import tabulate

conn = sqlite3.connect("band.db")
c=conn.cursor()


def main():
    print("Welcome to the bank!")
    kvb = bank("KVB")
    cus = kvb.all_cus()
    while True:
        choice = int(input("select option:\n    1) new customer\n    2)existing customer\n    3)exit\n"))

        if choice == 1:
            
        
            name = input("Enter name: ")
            acc_no = int(input("Enter account number: "))
            pin = input("Create a new 4-digit pin: ")
            balance = float(input("Enter the cash you like to deposit: "))
            
            branch = input("Enter branch name: ")
            baka = customer(acc_no, name, balance, branch, pin)
            kvb.add_cus(baka)
            baka.show_details() 

        elif choice ==2:
            x,attempts = 0,3

            while x!=1 and attempts > 0:
                name = input("enter name:  ")
                acc_no = int(input("enter account number:  "))
                
                pin = input("enter pin:  ")

                is_customer, customer_details = kvb.check_cus(name, acc_no, pin)
                if is_customer:
                    baka = customer(*customer_details)

                    x = True
                    break
                else:
                    print("customer not found, please try again...")
                    attempts -= 1
                    print(f"{attempts} attempts left")
                
            if x == True:
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
                        baka.deposit(amount)
                        time.sleep(0.5)
                        print("amount deposited successfully!")
                    elif choice == 2:
                        amount = float(input("enter the amount you like to withdraw: "))
                        time.sleep(0.5)
                        baka.withdraw(amount)
                    elif choice == 3:
                        time.sleep(0.5)
                        baka.show_details()
                    elif choice == 4:
                        new_pin = input("create a new 4-digit pin:  ")
                        baka.pin = new_pin
                        time.sleep(0.5)
                        print("pin changed successfully!")
                    elif choice == 5:
                        time.sleep(0.5)
                        baka.show_transaction_history()
                    elif choice == 6:
                        time.sleep(0.5)
                        print("thank you for banking with us!")
                        exit()
                        break
                    else:
                        print("invalid option, please try again.")
        elif choice == 3:
            print("thank you for banking with us!")
            exit()

    
                    
class customer():

    c.execute("""CREATE TABLE IF NOT EXISTS transaction_history(
              acc_no INTEGER NOT NULL,
              type TEXT NOT NULL,
              amount REAL NOT NULL,
              date text NOT NULL,
              time TEXT NOT NULL             
              
              )""")

    
    def __init__(self,acc_no, name, balance, branch, pin):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance
        self.branch = branch
        self.pin = pin
        
        for ifsc, name in bank.branch.items():
            if self.branch == name:
                self.ifsc = ifsc
                break
    
    def deposit(self, amount):
            self.balance += amount

            
            c.execute("update customers set balance = ? where acc_no = ?", (self.balance, self.acc_no))
            c.execute("insert into transaction_history values(?, ?, ?, ?, ?)", (self.acc_no,'Deposit', amount, datetime.now().strftime("%Y-%m-%d"), datetime.now().strftime("%H:%M:%S")))
            conn.commit()
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            
            c.execute("update customers set balance = ? where acc_no = ?", (self.balance, self.acc_no))
            c.execute("insert into transaction_history values(?, ?, ?, ?, ?)", (self.acc_no,'Withdraw', amount, datetime.now().strftime("%Y-%m-%d"), datetime.now().strftime("%H:%M:%S")))
            conn.commit()
            print("amount withdrawn successfully!")
        else:
            print("Insufficient balance")

    
    def check_c(self, name, acc_no, pin):
        
        if self.pin == pin and self.name == name and self.acc_no == acc_no:
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
        c.execute("select * from transaction_history where acc_no = ?" ,(self.acc_no,))
        hmm = c.fetchall()
        row = [(i[0], i[1], f"₹ {i[2]:.2f}", i[3], i[4]) for i in hmm]

        print(tabulate(row, headers = ['Account Number', 'Type', 'Amount', 'Date', 'Time'], tablefmt = 'rounded_grid'))

class bank():
    branch = {"IFSC001": "KVB Main Branch", "IFSC002": "KVB City Branch", "IFSC003": "KVB Sub Branch"}

    c.execute("""CREATE TABLE IF NOT EXISTS customers(
                acc_no INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                balance REAL NOT NULL,
                branch TEXT NOT NULL,
                pin TEXT NOT NULL
                )""")
    
    c.execute("""INSERT OR IGNORE INTO customers VALUES (123456, "Alice", 1000, "KVB Main Branch", "1234")""")
    c.execute("""INSERT OR IGNORE INTO customers VALUES (123457, "Bob", 500, "KVB City Branch", "5678")""")
    conn.commit()
    

    

    def __init__(self, b_name):
        self.b_name = b_name
        self.balance = 0
        
        

    def add_cus(self , customer):
        c.execute("INSERT INTO customers VALUES (?, ?, ?, ?, ?)", (customer.acc_no, customer.name, customer.balance, customer.branch, customer.pin))
        conn.commit()
        
    def check_cus(self, name, acc_no, pin):
        c.execute("select * from customers where acc_no = ?and name = ? and pin = ?", (acc_no, name, pin))
        yohohoho = c.fetchone()
        if yohohoho is not None:

            return True, yohohoho
        else:
            return False, None
        
    def all_cus(self):
        c.execute("select * from customers")
        hmm = c.fetchall()
        row = [(i[0], i[1], f"₹ {i[2]}", i[3]) for i in hmm]
        print(tabulate(row, headers = ['Account Number', 'Name', 'Balance', 'Branch'], tablefmt = 'rounded_grid'))




if __name__ =="__main__":
    main()
    conn.commit()
    conn.close()
    c.close()