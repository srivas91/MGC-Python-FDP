balance=0
def deposit():
    global balance
    amount=int(input('enter amount:'))
    balance=balance+amount
    balcheck()
#2.withdraw
def withdraw():
    global balance
    amount=int(input('enter amount:'))
    balance=balance-amount
    balcheck()

#3.balance
def balcheck():
    global balance
    print('available balance:',balance)
def menu():
    ch=0
    while(ch!=4):
        print("1.Deposit\n2.Withdraw\n3.Balance")
        ch=int(input("enter your choice:"))
        if ch==1:
            deposit()
        elif ch==2:
            withdraw()
        elif ch==3:
            balcheck()

from colorama import Fore, Back, Style

def welcome():
    print(Fore.BLUE+"welcome to MGC ATM:")
    pin = int(input('enter your ATM pin number:'))
    if pin == 123:
        menu()
    else:
        print('invalid pin number')
        welcome()
#enter your ATM pin number:
# 123

welcome()





