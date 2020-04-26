class BankSys:

    bank = "TD BANK"
    user = 'admin'
    Password = "123"

    def __init__(self, u, p):
        self.user=u
        self.password=p
        self.balance=0

    def UserConfig(self):
        if BankSys.user == self.user and BankSys.Password == self.password:
            return True
        else:
            return False

    def deposit(self,balance = 0 ):
        self.balance = balance
        print(self.balance)

    def Balance(self):
        if self.balance != 0:
            print("balance: ", self.balance)
        else:
            print("You Have 0 Balance")

    def withdrawal(self,wAmount):
        #print(wAmount)
        if wAmount < self.balance:
            self.balance -= wAmount
            print("${} Withdrawal success".format(wAmount))
        else:
            print("Account balance low \n to check account balance type B ")