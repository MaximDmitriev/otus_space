from interfaces.command import Command
from errors.error_handler import BaseAppException
from interfaces.fuelable import Fuelable

class BurnFuel(Command):
    '''
    команда расхода топлива
    '''

    def __init__(self, obj: Fuelable) -> None:
        self.obj = obj

    def execute(self):
        try:
            volume = self.obj.get_fuel_volume()
            unit = self.obj.get_fuel_unit()
        except Exception:
            raise BaseAppException("property cannot be read")
        
        try:
            self.obj.set_fuel_volume(volume - unit)
        except Exception:
            raise BaseAppException("property cannot be set")
