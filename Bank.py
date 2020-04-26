import sys
from banksys import BankSys

print(BankSys.bank)

u = input("Type UserName: ")
p = input("Type PassWord: ")
b = BankSys(u,p)
if b.UserConfig():
    while True:
        x = input("B for Balance | D for Deposit | W for Withdrawal | Q for Exit: ")

        if x == "b" or x =="B":
            b.Balance()

        elif x == "d" or x =="D":
            b.deposit(float(input("Input Amount: ")))

        elif x == "w" or x =="W":
            b.withdrawal(float(input("Input Amount: ")))

        elif x == "Q" or x =="q":
            print("Exit")
            sys.exit()
        else:
            print("Wrong Entry")
            sys.exit()
else:
    print("User or Password does not match")
    sys.exit()



