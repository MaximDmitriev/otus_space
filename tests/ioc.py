import unittest
from dataclasses import dataclass
from interfaces.command import Command
from ioc.ioc import IoC
from errors.error_handler import CmdNotFoundException

@dataclass
class TestCommand(Command):
    var: int

    def execute(self):
        return self.var + 1
    


class TestIoCRootScope(unittest.TestCase):
    '''Тесты для IoC для основного скоупа'''
    def setUp(self):
        self.ioc = IoC()

    def test_exec_registered_command(self):
        '''проверка выполнения зарегистрированной команды'''

        self.ioc.resolve('ioc.register', 'inc', lambda x: TestCommand(x)).execute()

        result = self.ioc.resolve('inc', 5).execute()

        self.assertEqual(result, 6)

    def test_raise_excepion_unregistered_command(self):
        '''выбрасывает исключение на незарегистрированной команде'''

        with self.assertRaises(CmdNotFoundException):
            self.ioc.resolve('unregistered', 5).execute()

    def test_raise_excepion_register_existing_command(self):
        '''выбрасывает исключение при попытке зарегистрировать существующую команду'''

        self.ioc.resolve('ioc.register', 'sum', lambda x: TestCommand(x)).execute()

        with self.assertRaises(KeyError):
            self.ioc.resolve('ioc.register', 'sum', lambda x: x + 1).execute()


class TestIoCChildren(unittest.TestCase):
    '''Тесты для дочерних скоупов'''

    def setUp(self):
        self.ioc = IoC()
        self.ioc.resolve('scopes.create', 'root', 'child').execute()


    def test_child_exec(self):
        '''дочерний скоуп может выполнить свой метод'''

        self.ioc.resolve('scopes.set', 'child').execute()
        self.ioc.resolve('ioc.register', 'child_inc', lambda x: TestCommand(x)).execute()

        result = self.ioc.resolve('child_inc', 10).execute()

        self.assertEqual(result, 11)

    def test_child_exec_root_func(self):
        '''дочерний скоуп может выполнить рутовый метод'''
        self.ioc.resolve('scopes.set', 'root').execute()
        self.ioc.resolve('ioc.register', 'root_inc', lambda x: TestCommand(x)).execute()

        result = self.ioc.resolve('root_inc', 15).execute()

        self.assertEqual(result, 16)

    def test_child_not_effect_root(self):
        '''дочерний скоуп не влияет на рутовый'''

        self.ioc.resolve('scopes.set', 'root').execute()

        with self.assertRaises(CmdNotFoundException):
            self.ioc.resolve('child_inc', 10).execute()