from interfaces.command import Command
from interfaces.fuelable import Fuelable
from errors.error_handler import BaseAppException

class CheckFuel(Command):
    '''
    команда проверки топлива
    '''

    def __init__(self, obj: Fuelable) -> None:
        self.obj = obj

    def execute(self):
        try:
            volume = self.obj.get_fuel_volume()
            unit = self.obj.get_fuel_unit()
        except Exception:
            raise BaseAppException("property cannot be read")
        
        if volume >= unit:
            return
        else:
            raise BaseAppException("Fuel is empty")