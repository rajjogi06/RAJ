class Bank(object):
    name=""
    acctno=0
    initial_bal=0.0
    amt=0
    def deposit(self,initial_bal,amt):
        X = self.initial_bal+self.amt
        return X

    def withdraw(self,initial_bal,amt):
        X = self.initial_bal-self.amt
        return X
        
    def accept(self):
        print("WELCOME TO ABC BANK")
        print("   ")
        print("PLEASE ENTER YOUR DETAILS")
        self.name=input("ENTER YOUR NAME = ")
        self.acctno=int(input("ENTER YOUR ACCOUNT NO. = "))
        self.initial_bal=5000
        print("YOUR BALANCE IS = ",self.initial_bal)
        print("Customer Details")
        print("NAME = ",self.name,"                ACCOUNT NO. = ",self.acctno) 
        print("CURRENT BALANCE = ",self.initial_bal)
        print("   ")
        print("1.withdraw")
        print("2.deposit")
        
        self.choice = input("ENTER THE CHOICE(1/2): ")
        
    if choice==1:
        print("enter amount to be deposited")
        self.amt = int(input())
        self.initial_bal=self.initial_bal+self.amt
        print("update balance is",deposit(self.initial_bal+self.amt))
    elif choice==2:
        print("enter amount to be withdraw")
        self.amt = int(input())
        self.initial_bal=self.initial_bal-self.amt
        print("update balance is",withdraw(self.initial_bal-self.amt))

    else:
        print("PLEASE SELECT THE OPERATOR")

b1=Bank()
b1.accept()
b1.choice()

