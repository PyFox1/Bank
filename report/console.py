from report.base import AbstractReport


class ConsoleLog(AbstractReport):
    def log(self, msg):
        print(msg)