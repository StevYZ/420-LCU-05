"""
Steven Yang-Zong 1931679
420-LCU COmputer Programming, Section-01
S.Hilal, instructor
Assignment 4
"""
import datetime

class BankAccount(object):
    __count = 0 #Number of instances
    def __init__ (self, ACCID, BKNAME, ACCTYPE, BAL = 0):
        self.ID = ACCID
        self.BankName = BKNAME
        self.type = ACCTYPE
        self.balance = BAL
        self.__pwd = ""
        self.__LastAccess = datetime.datetime.now()
        BankAccount.__count += 1

        #create a log in another file
        log = "{} {:6s} {:10s} {:7d} {:7d}".format(self.__LastAccess,self.ID,"create",0,self.balance)
        logfile = open("MyAccounts.txt","a+")
        print(log, file = logfile)
        logfile.close()

    def __del__ (self):
        BankAccount.__count -= 1
        print("Deleting Account Instances.")

    def __repr__ (self):
        """Creates and Returns the display string about a specific account"""
        format_str = "Bank ID: {:6s}, Bank: {:10s}, Account Type: {:10s}, Account Balance: {:7d}, Last Access: {}"
        d = format_str.format(self.ID, self.BankName, self.type, self.balance, self.__LastAccess)
        return (d)

    def deposit (self, amount):
        """Deposit amount into current account"""
        self.balance += amount
        print("Deposit of {0} accepted in {1}. Current balance is ${2}".format(amount, self.ID, self.balance))

        log = "{} {:6s} {:10s} {:7d} {:7d}".format(self.__LastAccess,self.ID,"deposit", amount,self.balance)
        logfile = open("MyAccounts.txt","a+")
        print(log, file = logfile)
        logfile.close()

    def withdraw (self, amount):
        """Withdraw amount from current account"""
        if (self.balance - amount) >= 0: #could be replaced by a global variable min_balance
            self.balance -= amount
            self.__LastAccess = datetime.datetime.now()
            print("Withrawal of {0} accepted in {1}. Current balance in account is: {2}".format(amount, self.ID, self.balance))

            log = "{} {:6s} {:10s} {:7d} {:7d}".format(self.__LastAccess,self.ID,"withdraw", amount,self.balance)
            logfile = open("MyAccounts.txt","a+")
            print(log, file = logfile)
            logfile.close()

        elif (self.balance-amount) <= 0:
            print("Inssuficient Funds in your account to withdraw: ${}".format(amount))

        else:
            print("ERROR with withdrawal.")


    def transfer (self, amount, other):
        """Transfer Money to Another Account"""
        if self.balance >= amount:
            self.balance -= amount
            other.balance += amount
            print("Transfer of {0} from account ID: {1} to account ID: {2} completed".format(amount, self.ID, other.ID))

            log1 = "{} {:6s} {:10s} -{:7d} {:7d}".format(self.__LastAccess,self.ID, "transfer",amount,self.balance)
            log2 = "{} {:6s} {:10s} +{:7d} {:7d}".format(other.__LastAccess,other.ID,"transfer",amount,other.balance)
            logfile = open("MyAccounts.txt","a+")
            print(log1, file = logfile)
            print(log2, file = logfile)
            logfile.close()

        elif self.balance < amount:
            print("Inssuficient Funds to transfer. Current {0} account balance is: {1}".format(self.ID, self.balance))

        else:
            print("ERROR with Transfer of Funds")

    def get_balance (self):
        """Return Balance of Current Account"""
        return (self.balance)

    def get_count (self):
        """Returns the count of instances this class has been run"""
        return (BankAccount.__count)

    def set_password (self):
        """Setting a password for an account"""
        x = 0
        pwd = input("Enter a password: ")
        print("\n")
        if pwd.isalnum() and (8<=len(pwd)<=15) and pwd[0].isupper() and not pwd.isalpha() and pwd[-1].isdigit() and not pwd.isupper():
               print("Password accepted")
               self.__pwd = pwd
        else:
            print("Password rejected")
            return x

        log = "{} {:6s} {:10s} {:7d} {:7d}".format(self.__LastAccess,self.ID,"set_pwd", 0,self.balance)
        logfile = open("MyAccounts.txt","a+")
        print(log, file = logfile)
        logfile.close()

    def verify_password (self, inp_pwd):
        """Verify if entered password correspond to account password"""
        if inp_pwd == self.__pwd:
            return True
        else:
            return False

    def delete (self):
        """Deletes an account"""

        log = "{} {:6s} ACCOUNT DELETED".format(self.__LastAccess, self.ID)
        logfile = open("MyAccounts.txt","a+")
        print(log, file = logfile)
        logfile.close()

        MyAccounts_dict.pop(self.ID,0)

        print("Account Deleted")

MyAccounts_dict = {} #dictionary of accounts
while True:
    #MENU
    print(
    """
    Welcome to the My Money Management App

    1- Create an account (Enter Account ID, Bank Name, Account Type, and Balance)
    2- Withdraw an amount from an account. (Enter Account ID, and Amount)
    3- Deposit an amount to an account. (Enter Accounf ID, and Amount)
    4- Transfer an amount between accounts (Enter From:, and Amount, and To: Accounts)
    5- Get balance of a given account (Enter Account ID)
    6- Delete an account (Enter Account ID)
    7- Display the log file.

    8- Exit the program
    """)

    menu_inp = input("Select an option by entering its number or 8 to exit: ")
    print("\n")

    #creating an account
    if menu_inp == "1":
        account = input("Enter account informations seperated by commas only (Account ID,Bank Name,Account Type,Balance in Account): ")
        account = account.split(",")
        print("\n")

        #Verify each account information
        validity = 1
        if account[0] in MyAccounts_dict:
            print("ERROR, Duplicate Account Number")
            validity = 0
        elif len(account[0]) != 6:
            print("INVALID account ID")
            validity = 0
        elif len(account[1]) < 2 or len(account[1]) > 8:
            print("INVALID Bank Name")
            validity = 0
        elif account[2] not in ["chequing", "saving", "investment", "loan", "TFSA", "RRSP"]:
            print("INVALID Account Type")
            validity = 0

        if validity == 1:
            #puts account into the dictionary
            a = BankAccount(account[0], account[1], account[2], int(account[3]))
            MyAccounts_dict[account[0]] = a

            #Set a password for the dictionary
            x = MyAccounts_dict[account[0]].set_password()

            print("\n")

            if x == 0:
                MyAccounts_dict[account[0]].delete()

            else:
                print("Bank account has been successfully created")

                print(MyAccounts_dict[account[0]])

    #withdrawing from an account
    elif menu_inp == "2":
        withdraw_inp = input("Enter account ID and withdraw amount seperated by commas only: ")
        withdraw_inp = withdraw_inp.split(",")

        inp_pwd = input("Account Password:")
        print("\n")

        #verify password and then execute withdraw function
        if MyAccounts_dict[withdraw_inp[0]].verify_password(inp_pwd):
            print("Password Accepted")
            MyAccounts_dict[withdraw_inp[0]].withdraw(int(withdraw_inp[1]))

        else:
            print("Incorrect Password")

    #depositing into an account
    elif menu_inp == "3":
        dep = input("Enter account informations seperated by commas only: ")
        dep = dep.split(",")

        inp_pwd = input("Account Password:")
        print("\n")

        #verify password and executing deposit function
        if MyAccounts_dict[dep[0]].verify_password(inp_pwd):
            print("Password Accepted")
            MyAccounts_dict[dep[0]].deposit(int(dep[1]))

        else:
            print("Incorrect Password")

    #transfer set amount from account 1 to account 2
    elif menu_inp == "4":
        acctrans1 = input("Enter account ID of the account transfering the funds with the amount seperated by commas only (Account ID, Amount): ")
        acctrans1 = acctrans1.split(",")
        acctrans2 = input("Enter account ID of the account receiving the funds: ")

        print("\n")
        inp_pwd = input("Transfering Account Password:")
        print("\n")

        #verify password of account 1 and executing transfer function
        if MyAccounts_dict[acctrans1[0]].verify_password(inp_pwd):
            print("Password Accepted")
            MyAccounts_dict[acctrans1[0]].transfer(int(acctrans1[1]), MyAccounts_dict[acctrans2])

        else:
            print("Incorrect Password")

    #Obtaining a balance of an account
    elif menu_inp == "5":
        acc_bal = input("Enter account number to obtain the balance on it: ")

        inp_pwd = input("Account Password:")
        print("\n")

        #verify account password and executing acc_bal function
        if MyAccounts_dict[acc_bal].verify_password(inp_pwd):
            print("Password Accepted")
            acbal = MyAccounts_dict[acc_bal].get_balance()
            print("The balance in account {0} is of ${1}".format(acc_bal, acbal))

        else:
            print("Incorrect Password")

    #deleting an account
    elif menu_inp == "6":
        del_acc = input("Enter account ID of the account that needs to be deleted: ")

        inp_pwd = input("Account Password:")
        print("\n")

        #verify password and executing delete function
        if MyAccounts_dict[del_acc].verify_password(inp_pwd):
            print("Password Accepted")
            MyAccounts_dict[del_acc].delete()

        else:
            print("Incorrect Password")

    #prints out the log file
    elif menu_inp == "7":
        fp1 = open("MyAccounts.txt")
        print(fp1.read())
        fp1.close()

    #exit the menu
    elif menu_inp == "8":
        print("Thank you for using My Money Management")
        exit()

    else:
        print("ERROR in menu options")
