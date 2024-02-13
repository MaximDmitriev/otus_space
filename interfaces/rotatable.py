from abc import ABC, abstractmethod
from htypes.vector import Vector

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

    @abstractmethod
    def set_velocity(self, vector: Vector) -> None:
        pass

    @abstractmethod
    def get_velocity(self) -> Vector:
        pass