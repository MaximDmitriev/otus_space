from commands.scope import NewScopeCommand, SetCurrentScopeCommand, FindScopeCommand, IoCRegisterCommand
from errors.error_handler import ScopeNotFoundException, CmdNotFoundException
from ioc.scope import Scope, ThreadData

DEFAULT_STRATEGY = {
    "scopes.create": lambda *args: NewScopeCommand(*args),
    "scopes.set": lambda *args: SetCurrentScopeCommand(id=args[0]),
    "scopes.find": lambda *args: FindScopeCommand(*args),
    "ioc.register": lambda *args: IoCRegisterCommand(key=args[0], command=args[1]),
}
   

class IoC:
    '''
    Контейнер инверсии зависимотей
    '''

    def __new__(cls):
        '''синглтон'''
        if not hasattr(cls, 'instance'):
            cls.instance = super(IoC, cls).__new__(cls)
        return cls.instance


    def __init__(self):
        root_scope: Scope = Scope(name="root").set_strategy(DEFAULT_STRATEGY)
        ThreadData.root_scope = root_scope
        ThreadData.current_scope = root_scope

    def resolve(self, key: str, *args: any):
        if not ThreadData.current_scope:
            raise ScopeNotFoundException('scope not found')

        for scope in ThreadData.current_scope:
            resolver = scope.strategy.get(key)

            if resolver:
                return resolver(*args)
            
        raise CmdNotFoundException(f'{key} command not found')
    


