import unittest
from unittest.mock import MagicMock
from commands.burn_fuel import BurnFuel
from adapters.fuelable import FuelableAdapter

class TestBurnFuel(unittest.TestCase):
    '''
    тесты для команды расхода топлива
    '''

    def test_fuel_burn(self):
        '''корректно вычисляет оставшийся объем топлива'''

        adapter = MagicMock(spec=FuelableAdapter)
        command = BurnFuel(adapter)

        adapter.get_fuel_volume.return_value = 4
        adapter.get_fuel_unit.return_value = 1

        command.execute()

        adapter.set_fuel_volume.assert_called_with(3)