class Account:
    _balance = 0
    _log = None

    def __init__(self, balance, **kwargs):
        self._balance = balance

        if "log" in kwargs:
            self._log = kwargs["log"]
        self._log.log("Account open")

    def deposit(self, amount):
        self._balance = self._balance + amount

    def get_balance(self):
        return self._balance

    def withdraw(self, amount):
        raise NotImplementedError

    def transfer(self, amount, target):
        self.withdraw(amount)
        target.deposit(amount)

    def do_actual_withdraw(self, amount):
        self._balance = self._balance - amount


class CheckingAccount(Account):
    _disposable_credit = 0

    def __init__(self, balance, **kwargs):
        super(CheckingAccount, self).__init__(balance, **kwargs)

        if "disposable_credit" in kwargs:
            self._disposable_credit = kwargs["disposable_credit"]


    def withdraw(self, amount):
        if (self._balance + self._disposable_credit - amount) < 0:
            raise ValueError("Cant withdraw")

        self.do_actual_withdraw(amount)


class PassbookAccount(Account):
    def withdraw(self, amount):
        if (self._balance - amount) < 5:
            self._log.log("ERROR: Cant withdraw\n")
            raise ValueError("Cant withdraw")

        self._log.log("INFO: withdraw %d\n" % amount)
        self.do_actual_withdraw(amount)
