from abc import ABC, abstractmethod

class Rotatable(ABC):
    '''
    интерфейс для вращающихся объектов
    '''

    @abstractmethod
    def get_direction(self) -> int:
        pass

    @abstractmethod
    def get_angular_velocity(self) -> int:
        pass

    @abstractmethod
    def get_direction_numbers(self) -> int:
        pass

    @abstractmethod
    def set_direction(self, direction: int) -> None:
        pass