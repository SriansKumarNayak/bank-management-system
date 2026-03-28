import json

class Account:

    account_no_counter = 1001

    def __init__(self, holder_name, balance, pin):
        self.account_no = Account.account_no_counter
        self.holder_name = holder_name
        self.balance = balance
        self.pin = pin

        Account.account_no_counter += 1

    def display(self):
        print(f"Account No: {self.account_no}\nName: {self.holder_name}\nBalance: ₹{self.balance}")

def save_accounts():
    data = []

    for acc in accounts:
        data.append({
            "account_no" : acc.account_no,
            "holder_name" : acc.holder_name,
            "balance" : acc.balance,
            "pin" : acc.pin
        })
        
    with open('accounts.json', 'w') as file:
        json.dump(data, file, indent = 4)

def load_accounts():
    try:
        with open('accounts.json', 'r') as file:
            data = json.load(file)

            for item in data:
                acc = Account(
                    item['holder_name'],
                    item['balance'],
                    item['pin']
                )
                acc.account_no = item['account_no']
                accounts.append(acc)

            if accounts:
                Account.account_no_counter = accounts[-1].account_no + 1
    except (FileNotFoundError, json.JSONDecodeError):
        pass

accounts = []
load_accounts()

while True:
    print("\n===== Bank Management System =====\n")
    print("1. Create Accounts")
    print("2. View Accounts")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Transfer")
    print("6. Exit")

    while True:
        try:
            choice = int(input("Enter Your Choice (1-6): "))
            break
        except ValueError:
            print("\nChoose from (1-6) only...\n")
        
    if choice == 1:
        print("\n===== Create Account =====\n")
        while True:
            name = input("Enter Your Name (or type '0' to cancel): ").strip()
            if name == "0":
                break
            elif name:
                break
            else:
                print("\nName cannot be empty!\n")
        if name == "0":
            continue
                
        while True:
            pin = input("Set 4-digit PIN: ").strip()
            if pin.isdigit() and len(pin) == 4:
                break
            
            if not pin.isdigit():
                print("\nEnter Number Only...\n")
            
            else:
                print("\nPIN must be exactly 4 digits\n")

        while True:
            try:
                balance = float(input("Enter Initial Balance: ₹"))
                if balance < 0:
                    print("\nBalance cannot be negative!\n")
                    continue
                break
            except ValueError:
                print("\nInvalid amount! Enter a number.\n")

        accounts.append(Account(name, balance, pin))
        save_accounts()

        print("\n-------------------------------")
        print("Account Created Successfully!\n")
        print(f"Account No: {accounts[-1].account_no}")
        print(f"Name: {accounts[-1].holder_name}")
        print(f"Current Balance: ₹{accounts[-1].balance}")
        print("-------------------------------\n")

    elif choice == 2:
        print("\n===== Account Records =====\n")
        if not accounts:
            print("No Record Found!")
        else:
            print("-------------------------------")
            for account in accounts:
                account.display()
                print("-------------------------------")

    elif choice == 3:
        print("\n===== Deposit Money =====\n")

        try:
            acc_no = int(input("Enter Account No (or type '0' to cancel): "))
        except ValueError:
            print("\nInvalid Account Number!\n")
            continue

        if acc_no == 0:
            continue

        found = False
        for account in accounts:
            if account.account_no == acc_no:
                found = True
                
                while True:
                    try:
                        amount = float(input("Enter amount to deposit: ₹"))
                        if amount <= 0:
                            print("\nAmount must be greater than 0!\n")
                            continue
                        break
                    except ValueError:
                        print("\nInvalid amount\n") 
                

                pin = input("Enter PIN to confirm: ").strip()
                if pin == account.pin:
                    account.balance += amount
                    save_accounts() 
                    print(f"\n₹{amount} Deposited Successfully")
                    print(f"Current Balance: ₹{account.balance}")  
                else:
                    print("\nIncorrect PIN! Transaction Cancelled.\n")

                break
    
        if not found:
            print("\nAccount Not Found!\n")

    elif choice == 4:
        print("\n===== Withdraw Money =====\n")
    
        try:
            acc_no = int(input("Enter Account No (or type '0' to cancel): "))
        except ValueError:
            print("\nInvalid Account Number!\n")
            continue

        if acc_no == 0:
            continue

        found = False
        for account in accounts:
            if account.account_no == acc_no:
                found = True
                
                while True:
                    try:
                        amount = float(input("Enter amount to withdraw: ₹"))
                        if amount > account.balance:
                            print("\nInsufficient Balance!\n")
                            continue
                        elif amount <= 0:
                            print("\nAmount must be greater than 0!\n")
                            continue
                        break
                    except ValueError:
                        print("\nInvalid amount\n") 
                

                pin = input("Enter PIN to confirm: ").strip()
                if pin == account.pin:
                    account.balance -= amount
                    save_accounts() 
                    print(f"\n₹{amount} Withdrawn Successfully")
                    print(f"Current Balance: ₹{account.balance}")  
                else:
                    print("\nIncorrect PIN! Transaction Cancelled.\n")

                break
    
        if not found:
            print("\nAccount Not Found!\n")

    elif choice == 5:
        print("\n===== Transfer Money =====\n")
        while True:
            try:
                sender_acc = int(input("Enter Your Account No (or type '0' to cancel): "))
                break
            except ValueError:
                print("Invalid Account Number!")
                continue
        if sender_acc == 0:
            continue

        sender = None
        for account in accounts:
            if account.account_no == sender_acc:
                sender = account
                break

        if not sender:
            print("\nSender Account Not Found!\n")
            continue

        while True:
            try:
                receiver_acc = int(input("Enter Receiver Account No: "))
                break
            except ValueError:
                print("Invalid Account Number!")
                continue

        receiver = None
        for account in accounts:
            if account.account_no == receiver_acc:
                receiver = account
                break

        if not receiver:
            print("\nReceiver Account Not Found!\n")
            continue

        if sender.account_no == receiver.account_no:
            print("\nCannot transfer to same account!\n")
            continue

        while True:
            try:
                amount = float(input("Enter amount to transfer: ₹"))
                if amount <= 0:
                    print("\nAmount must be greater than 0!\n")
                    continue
                elif amount > sender.balance:
                    print("\nInsufficient balance!\n")
                    continue
                break
            except ValueError:
                print("\nInvalid amount!\n")

        pin = input("Enter Your PIN to confirm: ").strip()
        if pin == sender.pin:
            sender.balance -= amount
            receiver.balance += amount
            save_accounts()
            print(f"\n₹{amount} transferred from Acc_no: {sender.account_no} to Acc_no: {receiver.account_no} Successfully")
            print(f"Your Current Balance: ₹{sender.balance}")
        else:
            print("\nIncorrect PIN! Transaction Cancelled.\n")

    elif choice == 6:
        print("\nThank You... Bye!")
        break
    else:
        print("\nChoose from (1-6) only...\n")