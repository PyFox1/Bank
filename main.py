import banking.accounts
from report.factory import build

passbook = banking.accounts.PassbookAccount(200, log=build())
checking = banking.accounts.CheckingAccount(500000, log=build())

checking.transfer(500, passbook)
print(passbook.get_balance())