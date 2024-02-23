from interfaces.command import Command
from dataclasses import dataclass
from ioc.scope import ThreadData, Scope
from errors.error_handler import ScopeNotFoundException

class FindScopeCommand(Command):
    '''
    Поиск скоупа по наименованию/идентификатору
    '''

    def __init__(self, id: str) -> None:
        self.id = id

    def execute(self):
        root = ThreadData.root_scope
        children = root.children

        if root.name == self.id:
            return root
        
        else:
            for scope in children:
                if scope.name == self.id:
                    return scope
        
        raise ScopeNotFoundException('scope not found')
    
    
class SetCurrentScopeCommand(Command):
    """
    Выбор текущего скоупа по наименованию/идентификатору
    """
    def __init__(self, id: str) -> None:
        self.id = id

    def execute(self):
        scope = FindScopeCommand(self.id).execute()
        ThreadData.current_scope = scope
        return scope


class NewScopeCommand(Command):
    """
    Добавление скоупа в качестве дочернего
    """

    def __init__(self, parent_id: str, id: str) -> None:
       self.parent_id = parent_id
       self.id = id

    def execute(self):
        parent_scope = FindScopeCommand(self.parent_id).execute()
        new_scope = Scope(name=self.id, parent=parent_scope)
        parent_scope.children.append(new_scope)

        return new_scope
    

@dataclass
class IoCRegisterCommand(Command):
    """
    команда регистрации новой зависимости в IoC
    """

    key: str
    command: callable

    def execute(self):
        active_scope = ThreadData.current_scope
        if self.key in active_scope.strategy:
            raise KeyError(f"{self.key} already registered!")
        active_scope.strategy[self.key] = self.command