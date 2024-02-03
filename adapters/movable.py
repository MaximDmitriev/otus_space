from htypes.vector import Vector
from interfaces.movable import Movable
from interfaces.gameobject import GameObject

class MovableAdapter(Movable):
    '''
    адаптер для движущихся объектов
    '''

    def __init__(self, obj: GameObject):
        self.obj = obj

    def get_location(self) -> Vector:
        return self.obj.get_property('location')

    def set_location(self, vector: Vector) -> None:
        self.obj.set_property('location', vector)

    def get_velocity(self) -> Vector:  
        return self.obj.get_property('velocity')