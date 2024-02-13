from interfaces.gameobject import GameObject
from interfaces.fuelable import Fuelable

class FuelableAdapter(Fuelable):
    '''
    адаптер для объектов с потреблением топлива
    '''

    def __init__(self, obj: GameObject):
        self.obj = obj

    def set_fuel_unit(self, volume: int) -> None:
        self.obj.set_property('fuel_unit', volume)

    def get_fuel_unit(self) -> int:
        return self.obj.get_property('fuel_unit')
    
    def set_fuel_volume(self, volume: int) -> None:
        self.obj.set_property('fuel_volume', volume)

    def get_fuel_volume(self) -> int:
        return self.obj.get_property('fuel_volume')