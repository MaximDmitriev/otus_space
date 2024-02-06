import unittest
from unittest.mock import MagicMock
from commands.move import Move
from adapters.movable import MovableAdapter
from htypes.vector import Vector
from interfaces.gameobject import GameObject

class TestMovable(unittest.TestCase):
    '''тест команды Move'''

    def test_set_location(self):
        '''проверка корректности расчета перемещения'''

        mock_movable = MagicMock(spec=MovableAdapter)
        move = Move(mock_movable)
        
        mock_movable.get_location.return_value = Vector(12, 5)
        mock_movable.get_velocity.return_value = Vector(-7, 3)

        move.execute()

        mock_movable.set_location.assert_called_with(Vector(5, 8))

    def test_invalid_location(self):
        '''при невозможности прочтения позиции выбрасывает исключение'''

        game_object = GameObject()
        game_object.set_property('location', Vector(12, 5))

        movable = MovableAdapter(game_object)
        move = Move(movable)

        with self.assertRaises(Exception):
            move.execute()

    def test_invalid_velocity(self):
        '''при невозможности прочтения скорости выбрасывает исключение'''

        game_object = GameObject()
        game_object.set_property('velocity', Vector(-7, 3))

        movable = MovableAdapter(game_object)
        move = Move(movable)

        with self.assertRaises(Exception):
            move.execute()