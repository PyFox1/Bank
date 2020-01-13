from report import file, console

file_log = file.FileLog()
console_log = console.ConsoleLog()


def build():
    return file_log
