import unittest
from unittest.mock import MagicMock
from commands.check_fuel import CheckFuel
from adapters.fuelable import FuelableAdapter

class TestCheckFuel(unittest.TestCase):
    '''
    тесты для команды проверки топлива
    '''

    def test_low_fuel(self):
        '''при недостатке топлива выбрасывает ошибку'''

        adapter = MagicMock(spec=FuelableAdapter)
        command = CheckFuel(adapter)

        adapter.get_fuel_volume.return_value = 1
        adapter.get_fuel_unit.return_value = 2

        with self.assertRaises(Exception):
            command.execute()