from bank_accounts import *

Dave = BankAccount(1000, "Dave")
Sara = BankAccount(2000, "Sara")

Dave.getBalance()
Sara.getBalance()

Sara.deposit(500)

Dave.withdraw(10000)
Dave.withdraw(10)

Dave.transfer(10000, Sara)
Dave.transfer(100, Sara)

Jim = IntrestRewardsAcct(1000, "Jim")

Jim.getBalance()

Jim.deposit(100)

Jim.transfer(100, Dave)

Blake = SavingsAcct(1000, "Blake")

Blake.getBalance()

Blake.deposit(100)

Blake.transfer(10000, Sara)
Blake.transfer(1000, Sara)