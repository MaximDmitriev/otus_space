import unittest
from unittest.mock import MagicMock
from commands.rotate import Rotate
from adapters.rotatable import RotatableAdapter
from interfaces.gameobject import GameObject

class TestRotatable(unittest.TestCase):
    '''тест команды Rotate'''

    def test_set_direction(self):
        '''проверка корректности расчета направления'''

        mock_rotatable = MagicMock(spec=RotatableAdapter)
        rotate = Rotate(mock_rotatable)

        mock_rotatable.get_direction.return_value = 3
        mock_rotatable.get_direction_numbers.return_value = 36
        mock_rotatable.get_angular_velocity.return_value = 23

        rotate.execute()

        mock_rotatable.set_direction.assert_called_with(26)

    def test_invalid_direction(self):
        '''при невозможности прочтения направления выбрасывает исключение'''

        game_object = GameObject()
        game_object.set_property('direction_numbers', 20)
        game_object.set_property('angular_velocity', 4)

        adapter = RotatableAdapter(game_object)
        rotate = Rotate(adapter)

        with self.assertRaises(Exception):
            rotate.execute()

    def test_invalid_direction_numbers(self):
        '''при невозможности прочтения единицы поворота выбрасывает исключение'''

        game_object = GameObject()
        game_object.set_property('direction', 20)
        game_object.set_property('angular_velocity', 4)

        adapter = RotatableAdapter(game_object)
        rotate = Rotate(adapter)

        with self.assertRaises(Exception):
            rotate.execute()

    def test_invalid_velocity(self):
        '''при невозможности прочтения скорости выбрасывает исключение'''

        game_object = GameObject()
        game_object.set_property('direction', 20)
        game_object.set_property('direction_numbers', 4)

        adapter = RotatableAdapter(game_object)
        rotate = Rotate(adapter)

        with self.assertRaises(Exception):
            rotate.execute()