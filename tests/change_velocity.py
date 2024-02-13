import unittest
from unittest.mock import MagicMock
from commands.change_velocity import ChangeVelocity
from adapters.rotatable import RotatableAdapter
from htypes.vector import Vector

class TestChangeVelocity(unittest.TestCase):
    '''
    тесты для команды изменения скорости при повороте
    '''

    def setUp(self):
        self.adapter = MagicMock(spec=RotatableAdapter)
        self.command = ChangeVelocity(self.adapter)

    def test_change_nonezero_velocity(self):
        '''если скорость ненулевая, то вектор меняется'''

        self.adapter.get_direction.return_value = 3
        self.adapter.get_direction_numbers.return_value = 20
        self.adapter.get_velocity.return_value = Vector(-7, 3)

        self.command.execute()

        self.adapter.set_velocity.assert_called_with(Vector(-11, 5))

    def test_not_change_zero_velocity(self):
        '''если скорость нулевая, то вектор не меняется'''

        self.adapter.get_direction.return_value = 3
        self.adapter.get_direction_numbers.return_value = 20
        self.adapter.get_velocity.return_value = Vector(0, 0)

        self.command.execute()

        self.adapter.set_velocity.assert_not_called()
