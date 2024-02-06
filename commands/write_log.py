from interfaces.command import Command

class WriteLog(Command):
    '''
    запись ошибки в лог
    '''

    def __init__(self, cmd, exc):
        self.cmd = cmd
        self.exc = exc

        self.cmd_name = self.cmd.__class__.__name__ if hasattr(self.cmd.__class__, __name__) else self.cmd.__class__
        self.exc_name = self.exc.__name__ if hasattr(self.exc, __name__) else self.exc

    def execute(self):
        print(
            f"Error: [[Command: {self.cmd_name}, "
            f"Exception: {self.exc_name}]]"
            f"\n"
        )