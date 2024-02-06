import unittest
from unittest.mock import Mock, MagicMock
from queue import Queue
from commands.write_log import WriteLog
from commands.move import Move
from adapters.movable import MovableAdapter
from errors.error_handler import ErrorHandler, BaseAppException
from commands.repeate import Repeate, RepeateHandler, DoubleRepeate


class TestExceptions(unittest.TestCase):
    '''тест обработчиков исключений'''

    def setUp(self):
        self.queue = Queue()
        mock_movable = MagicMock(spec=MovableAdapter)
        self.mock_move = MagicMock(spec=Move)

        self.move = Move(mock_movable)
        self.move.execute = MagicMock(side_effect=BaseAppException())

        self.handler = ErrorHandler()

        self.queue.put(self.move)


    def test_double_repeate(self):
        '''проверка стратегии вызов + двойной повтор, затем лог'''

        self.handler.register(Move, BaseAppException, lambda cmd, exc: RepeateHandler(DoubleRepeate(cmd), self.queue))
        self.handler.register(DoubleRepeate, BaseAppException, lambda cmd, exc: RepeateHandler(Repeate(cmd), self.queue))
        self.handler.register(Repeate, BaseAppException, lambda cmd, exc: RepeateHandler(WriteLog(cmd, exc), self.queue))

        while not self.queue.empty():
            cmd = self.queue.get()
            try:
                cmd.execute()

            except Exception as err:
                exc = type(err)

                self.handler.handle(cmd, exc)

        count = self.move.execute.call_count

        self.assertEqual(count, 3)

        
    def test_repeate(self):
        '''проверка стратегии вызов + повтор, затем лог'''

        self.handler.register(Move, BaseAppException, lambda cmd, exc: RepeateHandler(Repeate(cmd), self.queue))
        self.handler.register(Repeate, BaseAppException, lambda cmd, exc: RepeateHandler(WriteLog(cmd, exc), self.queue))

        while not self.queue.empty():
            cmd = self.queue.get()
            try:
                cmd.execute()

            except Exception as err:
                exc = type(err)

                self.handler.handle(cmd, exc)

        count = self.move.execute.call_count

        self.assertEqual(count, 2)