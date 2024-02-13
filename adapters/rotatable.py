from interfaces.rotatable import Rotatable
from interfaces.gameobject import GameObject
from htypes.vector import Vector

class RotatableAdapter(Rotatable):
    '''
    адаптер для вращающихся объектов
    '''

    def __init__(self, obj: GameObject):
        self.obj = obj

    def get_direction(self) -> int:
        return self.obj.get_property('direction')

    def get_angular_velocity(self) -> int:
        return self.obj.get_property('angular_velocity')

    def get_direction_numbers(self) -> int:
        return self.obj.get_property('direction_numbers')

    def set_direction(self, direction: int) -> None:
        self.obj.set_property('direction', direction)

    def set_velocity(self, vector: Vector) -> None:
        self.obj.set_property('velocity', vector)

    def get_velocity(self) -> Vector:
        return self.obj.get_property('velocity')