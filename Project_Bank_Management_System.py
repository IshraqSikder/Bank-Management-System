"""
Name : Md. Ishraq Uddin Sikder
Email : nirzon.sikderbd@gmail.com 

"""

import random

class User():
    def __init__(self) -> None:
        self.accounts = {}
    
    def create_account(self, name, email, address, acc_type):
        acc_number = random.randint(100,500)
        self.accounts[acc_number] = {
            "name" : name,
            "email" : email,
            "address" : address,
            "acc_type" : acc_type,
            "balance" : 0,
            "transaction" : [],
            "loan_count" : 0,
            "loan_amount" : 0
        }
        return acc_number
    
    def deposit(self, account, amount):
        if amount > 0 and account in self.accounts:
            self.accounts[account]["balance"] += amount
            self.accounts[account]["transaction"].append(f'Deposited {amount}')
            return True
        else:
            return False
    
    def withdraw(self,account,amount):
        if amount >= 0 and account in self.accounts and self.accounts[account]["balance"] >= amount:
            self.accounts[account]["balance"] -= amount
            self.accounts[account]["transaction"].append(f'Withdrew {amount}')
            return True
        else:
            return False
            
    def check_balance(self, account):
        if account in self.accounts:
            return self.accounts[account]["balance"]
        else:
            return None
    
    def transaction_history(self, account):
        if account in self.accounts:
            return self.accounts[account]["transaction"]
        else:
            return None
    
    def loan_taking(self, account, loan_amount):
        if not self.loan_feature_active:
            print("Loan feature is currently disabled.")
            return False
        if account in self.accounts:
            if self.accounts[account]["loan_count"] < 2:
                self.accounts[account]["loan_count"] += 1
                self.accounts[account]["balance"] += loan_amount
                self.accounts[account]["loan_amount"] += loan_amount
                self.accounts[account]["transaction"].append(f'Took loan {loan_amount}')
                return True
            else:
                print(f'{account} account cannot take loan anymore')
        else:
            print("Invalid Account")
           
    def transfer_amount(self, account, reciever, amount):
        if account in self.accounts:
            if reciever in self.accounts:
                if self.accounts[account]["balance"] >= amount:
                    self.accounts[reciever]["balance"] += amount
                    self.accounts[account]["balance"] -= amount
                    self.accounts[account]["transaction"].append(f'Transferred BDT{amount} to {reciever}')
                    print(f'BDT {amount} is transferred from {account} to {reciever}')
                else:
                    print('Insufficient Balance')
            else:
                print('Reciever is not found')
        else:
            print('Account does not exist')

def user_panel(obj):
    while True:
        print("\nUser Panel")
        print("1. Create an account")
        print("2. Deposit Amount")
        print("3. Withdraw Amount")
        print("4. Check Balance")
        print("5. Check Transaction History")
        print("6. Take a loan")
        print("7. Transfer Money")
        print("8. Back to the Main menu\n")
        opt=int(input('Enter your choice : '))
        if opt == 1:
            name = input("\nEnter your name: ")
            email = input("Enter your email: ")
            address = input("Enter your address: ")
            account_type = input("Enter account type (savings/current): ")
            user = obj.create_account(name,email,address,account_type)
            print(f'Account is created successfully. Your account number is: {user}\n')
        elif opt == 2:
            user = int(input("Enter your account number: "))
            deposit_taka = int(input('Enter deposited amount : '))
            if obj.deposit(user, deposit_taka):
                print(f'BDT{deposit_taka} is deposited successfully')
            else:       
                print('Invalid amount to deposit')
        elif opt == 3:
            user = int(input("Enter your account number: "))
            withdraw_taka = int(input('Enter withdrawn amount : '))
            if obj.withdraw(user, withdraw_taka):
                print(f'BDT{withdraw_taka} is withdrawn successfully')
            else:       
                print('Withdrawal amount exceeded')    
        elif opt == 4:
            user = int(input("Enter your account number: "))
            if obj.check_balance(user) is None:
                print('Invalid Account')
            else:
                print(f'Availble Balance : BDT{obj.check_balance(user)}')
        elif opt == 5:
            user = int(input("Enter your account number: "))
            if obj.transaction_history(user) is None:
                print('Invalid Account')
            else:
                print(f'Transaction History : {obj.transaction_history(user)}')
        elif opt == 6:
            user = int(input("Enter your account number: "))
            loan = int(input('Enter loan taking amount : '))
            if obj.loan_taking(user, loan):
                print(f'BDT{loan} loan is given successfully')
            else:
                print("Loan failed")   
        elif opt == 7:
            user = int(input("Enter your account number: "))
            reciever = int(input('Enter reciever account : '))
            transfer = int(input('Enter transfering amount : '))
            obj.transfer_amount(user, reciever, transfer)
        elif opt == 8:
            break
        else:
            print('Invalid choice. Please try again.')              
                 
class Admin:
    def __init__(self, obj_user) -> None:
        self.obj_user = obj_user
        
    def create_account(self, name, email, address, acc_type):
        return self.obj_user.create_account(name, email, address, acc_type)
    
    def delete_account(self, account):
        if account in self.obj_user.accounts:
            del self.obj_user.accounts[account]
            return True
        else:
            return False  
            
    def view_all_accounts(self):
        return self.obj_user.accounts

    def total_available_balance(self):
        balance_sum = sum(item['balance'] for item in self.obj_user.accounts.values())
        return balance_sum
    
    def total_loan_amount(self):
        loan_sum = sum(item['loan_amount'] for item in self.obj_user.accounts.values())
        return loan_sum
        
    def loan_feature(self, isLoanActive):
        self.obj_user.loan_feature_active = isLoanActive
        print(f'\nLoan feature is {'enabled' if isLoanActive else 'disabled'}')

 
def admin_panel(obj):
    while(True):
        print("\nAdmin Panel")
        print("1. Create an account")
        print("2. Delete an account")
        print("3. View all account")
        print("4. Check total available balance")
        print("5. Check total loan amount")
        print("6. Activate/Deactivate loan feature")
        print("7. Back to the Main menu\n")
        opt=int(input('Enter your choice : ')) 
        if opt == 1:
            name = input("\nEnter your name: ")
            email = input("Enter your email: ")
            address = input("Enter your address: ")
            account_type = input("Enter account type (savings/current): ")
            user = obj.create_account(name,email,address,account_type)
            print(f'\nAccount is created successfully. Your account number is: {user}\n')        
        elif opt == 2:
            user = int(input("Enter account number: "))
            if obj.delete_account(user):
                print("Account is deleted successfully")
            else:
                print("Invalid Account")
        elif opt == 3:
            info = obj.view_all_accounts()
            print("\nAll Accounts Details =>")
            for acc_number, details in info.items():
                print(f'Account Number: {acc_number}, Name: {details['name']}, Email: {details['email']}, Balance: {details['balance']}')
        elif opt == 4:
            print(f'\nTotal available balance : BDT{obj.total_available_balance()}')
        elif opt == 5:
            print(f'\nTotal loan amount : BDT{obj.total_loan_amount()}')
        elif opt == 6:
            isLoanActive = input("\nEnter 'on' to activate or 'off' to deactivate loan feature: ")
            obj.loan_feature(isLoanActive == 'on')
            
        elif opt == 7:
            break
        else:
            print('\nInvalid choice. Please try again.')
    
# Main Function   
def replica():
    print("\nWelcome to the Phitron Bank Management System")
    obj1 = User()
    obj2 = Admin(obj1)
    while(True):
        print("\n1. Click for User")
        print("2. Click for Admin")
        print("3. Exit")
        opt=int(input('Enter your choice : '))
        if opt == 1:
            user_panel(obj1)
        elif opt == 2:
            admin_panel(obj2)
        else:
            print('\nThank You')
            break
        
replica()