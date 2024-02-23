from typing import Callable
from interfaces.command import Command

class BaseAppException(Exception):
    pass


class ScopeNotFoundException(Exception):
    pass

class CmdNotFoundException(Exception):
    pass

class ErrorHandler:
    '''
    обработчик ошибок
    '''

    def __init__(self) -> None:
        self.mapper = {}

    def register(self, cmd: Command, exc: Exception, lambda_func: Callable) -> None:
        cmd_type = cmd.__name__
        exc_type = exc.__name__

        self.mapper[(cmd_type, exc_type)] = lambda_func


    def handle(self, cmd: Command, exc: Exception) -> None:
        cmd_key = cmd.__class__.__name__
        exc_key = exc.__name__
        lambda_func = self.mapper[(cmd_key, exc_key)]

        if lambda_func:
            lambda_func(cmd, exc).execute()
        else:
            raise exc