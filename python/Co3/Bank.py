class Bank:
    def __init__(self):
        self.accno = int(input("Enter the account number: "))
        self.accname = input("Enter the account name: ")
        self.acctype = input("Enter the account type: ")
        self.balance = 0

    def deposit(self):
        amount = int(input("Enter the deposit amount: "))
        self.balance = self.balance + amount
        print("\nAmount Deposited:", amount)

    def withdraw(self):
        amount = int(input("Enter amount to be withdrawn: "))
        if self.balance >= amount:
            self.balance = self.balance - amount
            print("\nAmount withdrawn is:", amount)
        else:
            print("\nInsufficient Balance")
            print("Current balance is:", self.balance)

    def display(self):
        print("Net Available balance =", self.balance)


B_Aobj = Bank()

while True:
    print("\n1. Deposit \n2. Withdraw \n3. View Balance \n4. Exit")
    ch = int(input("Enter your choice: "))
    
    if ch == 1:
        B_Aobj.deposit()
        B_Aobj.display()
    elif ch == 2:
        B_Aobj.withdraw()
        B_Aobj.display()
    elif ch == 3:
        B_Aobj.display()
    else:
        break






--------output-----------

Enter the account number: 1234
Enter the account name: aksa
Enter the account type: current

1. Deposit 
2. Withdraw 
3. View Balance 
4. Exit
Enter your choice: 1
Enter the deposit amount: 10000000

Amount Deposited: 10000000
Net Available balance = 10000000

1. Deposit 
2. Withdraw 
3. View Balance 
4. Exit
Enter your choice: 3
Net Available balance = 10000000

1. Deposit 
2. Withdraw 
3. View Balance 
4. Exit
Enter your choice: 2
Enter amount to be withdrawn: 5000

Amount withdrawn is: 5000
Net Available balance = 9995000

1. Deposit 
2. Withdraw 
3. View Balance 
4. Exit
Enter your choice: 
