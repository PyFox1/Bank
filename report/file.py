from report.base import AbstractReport


class FileLog(AbstractReport):
    def log(self, msg):
        with open("./data/transaction.log", "a") as f:
            f.write(msg)
