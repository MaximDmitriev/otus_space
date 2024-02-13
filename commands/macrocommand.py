from interfaces.command import Command
from errors.error_handler import BaseAppException

class MacroCommand(Command):
    """
    Макрокоманда
    """

    def __init__(self, commands):
        self.commands = commands

    def execute(self):
        for command in self.commands:
            try:
                command.execute()
            except Exception as error:
                raise BaseAppException(error)