class bank():
    branch = {"IFSC001": "KVB Main Branch", "IFSC002": "KVB City Branch"}
    def __init__(self, b_name):
        self.b_name = b_name
        self.balance = 0
        self.customers = {123456: customer(123456, "Alice", 1000, "KVB Main Branch", "1234"), 123457: customer(123457, "Bob", 500, "KVB City Branch", "5678")}
        self.num_customers = len(self.customers)

    def add_cus(self , customer):
        self.customers[customer.acc_no] = customer

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient balance")
    



class customer(bank):
    num_customers = 0
    def __init__(self,acc_no, name, balance, branch, pin):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance
        self.branch = branch
        self.pin = pin
        self.num_customers += 1
    


    def check_c(self, pin, name):
        if self.pin == pin and self.name == name:
            return True
        else:
            return False
    def show_details(self):
        print(f"\nAccount Number: {self.acc_no}")
        print(f"Name    : {self.name}")
        print(f"Branch  : {self.branch}")
        print(f"Balance : ₹{self.balance:.2f}")

    def show_transaction_history(self):
        pass