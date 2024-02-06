from interfaces.command import Command

class RepeateHandler:
    def __init__(self, cmd: Command, queue) -> None:
        self.cmd = cmd
        self.queue = queue

    def execute(self):
        self.queue.put(self.cmd)



class Repeate(Command):
    '''
    повтор команды
    '''

    def __init__(self, cmd: Command) -> None:
        self.cmd = cmd

    def execute(self):
        self.cmd.execute()

class DoubleRepeate(Command):
    '''
    двойной повтор команды
    '''

    def __init__(self, cmd: Command) -> None:
        self.cmd = cmd

    def execute(self):
        self.cmd.execute()
