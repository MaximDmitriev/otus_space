from abc import ABC, abstractmethod
from htypes.vector import Vector


class Movable(ABC):
    '''
    интерфейс для двигающихся объектов
    '''

    @abstractmethod
    def get_location(self) -> Vector:
        pass

    @abstractmethod
    def set_location(self, vector: Vector) -> None:
        pass

    @abstractmethod
    def set_velocity(self, vector: Vector) -> None:
        pass

    @abstractmethod
    def get_velocity(self) -> Vector:
        pass