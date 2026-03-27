class Account:

    account_number = 1001

    def __init__(self, holder_name, balance, pin):
        self.account_number = Account.account_number
        self.holder_name = holder_name
        self.balance = balance
        self.pin = pin

        Account.account_number += 1

    def display(self):
        print(f"Account No: {self.account_number}\nName: {self.holder_name}\nBalance: ₹{self.balance}")

accounts = []

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
            choice = int(input("Enter choice (1-6): "))
            break
        except ValueError:
            print("\nChoose from (1-6) only...\n")

    if choice == 1:
        print("\n===== Create Account =====\n")
        
        #Name Input
        while True:
            name = input("Enter Account Holder Name: ").strip()
            if name:
                break
            else:
                print("\nName cannot be empty!\n")
        
        #Balance Input
        while True:
            try:
                balance = float(input("Enter Initial Balance: "))
                if balance < 0:
                    print("Balance cannot be negative")
                    continue
                break
            except ValueError:
                print("\nInvalid amount! Enter a number.\n")

        #PIN set-up
        while True:
            pin = input("Set 4-digit PIN: ").strip()
            if pin.isdigit() and len(pin) == 4:
                break
            else:
                print("\nPIN must be exactly 4 digits\n")
                
        #Account Created
        accounts.append(Account(name, balance, pin))
        print("\n----------------------------------------")
        print("Account Created Successfully!")
        print(f"Account No: {accounts[-1].account_number}")
        print(f"Name: {accounts[-1].holder_name}")
        print("----------------------------------------")

    elif choice == 2:
        if not accounts:
            print("No Record Found!")
        else:
            print("\n--- Account Records ---")
            print("----------------------------------------")
            for account in accounts:
                account.display()
                print("----------------------------------------")

    elif choice == 3:
        print("\n===== Deposit Money =====\n")
        try:
            account_no = int(input("Enter Your Account Number: "))
        except ValueError:
            print("Invalid Account Number!")
            continue

        found = False
        for account in accounts:
            if account.account_number == account_no:
                found = True
                pin = input("Enter PIN: ").strip()
                if pin != account.pin:
                    print("\nIncorrect PIN!\n")  
                    break

                while True:
                    try:
                        amount = float(input("Enter amount to deposit: ₹"))
                        if amount <= 0:
                            print("Amount must be greater than 0!")
                            continue
                        break
                    except ValueError:
                        print("\nInvalid amount\n")

                account.balance += amount
                print(f"\n₹{amount} Deposited Successfully")
                print(f"Current Balance: ₹{account.balance}")
                break

        if not found:
            print("\nAccount Not Found!\n")

    elif choice == 4:
        print("\n===== Withdraw Money =====\n")
        try:
            account_no = int(input("Enter Your Account Number: "))
        except ValueError:
            print("Invalid Account Number!")
            continue
    
        found = False
        for account in accounts:
            if account.account_number == account_no:
                found = True
                pin = input("Enter PIN: ").strip()
                if pin != account.pin:
                    print("\nIncorrect PIN!\n")
                    break
                while True:
                    try:
                        amount = float(input("Enter amount to withdraw: ₹"))
                        if amount <= 0:
                            print("Amount must be greater than 0!")
                            continue
                        if amount > account.balance:
                            print("\nInsufficient Balance!\n")
                            continue
                        break
                    except ValueError:
                        print("\nInvalid amount!\n")

                account.balance -= amount
                print(f"\n₹{amount} Withdrawn Successfully!")
                print(f"Remaining Balance: ₹{account.balance}")
                break
        if not found:
             print("\nAccount Not Found!\n")

    elif choice == 5:
        print("\n===== Transfer Money =====\n")

        try:
            sender_acc_no = int(input("Enter Your Account Number: "))
        except ValueError:
            print("Invalid Account Number!")
            continue

        sender = None
        for account in accounts:
            if account.account_number == sender_acc_no:
                sender = account
                break
        
        if not sender:
            print("Sender account not found!")
            continue

        pin = input("Enter PIN: ").strip()
        if pin != sender.pin:
            print("\nIncorrect PIN!\n")
            continue

        try:
            receiver_acc_no = int(input("Enter Receiver Account Number: "))
        except ValueError:
            print("\nInvalid Account Number!\n")
            continue

        receiver = None
        for account in accounts:
            if account.account_number == receiver_acc_no:
                receiver = account
                break

        if not receiver:
            print("\nReceiver account not found!\n")
            continue

        if sender.account_number == receiver.account_number:
            print("\nCannot transfer to same account!\n")
            continue

        while True:
            try:
                amount = float(input("Enter amount to transfer: ₹"))
                if amount <= 0:
                    print("\nAmount must be greater than 0!\n")
                    continue
                if amount > sender.balance:
                    print("Insufficient balance")
                    continue
                break
            except ValueError:
                print("\nInvalid amount!\n")

        sender.balance -= amount
        receiver.balance += amount

        print(f"\n₹{amount} transferred from Acc_no: {sender.account_number} to Acc_no: {receiver.account_number} Successfully")
        print(f"Your Current Balance: ₹{sender.balance}")

    elif choice == 6:
        print("Thank You... Bye!")
        break
    else:
        print("\nChoose from (1-6) only...\n")

