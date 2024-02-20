from abc import ABC, abstractmethod

class Fuelable(ABC):
    '''
    интерфейс для объекта, потребляющего топливо
    '''

    @abstractmethod
    def get_fuel_volume(self) -> int:
        pass

    @abstractmethod
    def set_fuel_volume(self, volume: int) -> None:
        pass

    @abstractmethod
    def get_fuel_unit(self) -> int:
        pass

    @abstractmethod
    def set_fuel_unit(self, volume: int) -> None:
        pass