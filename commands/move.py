from interfaces.movable import Movable
from interfaces.command import Command
from htypes.vector import Vector
from errors.error_handler import BaseAppException


class Move(Command):
    '''
    команда прямолинейного движения
    '''

    def __init__(self, obj: Movable):
        self.obj = obj

    def execute(self) -> None:
        try:
            location = self.obj.get_location()
        except:
            raise BaseAppException("property 'location' cannot be read")

        
        try:
            velocity = self.obj.get_velocity()
        except:
            raise BaseAppException("property 'velocity' cannot be read")


        try:
            self.obj.set_location(Vector.plus(location, velocity))
        except:
            raise BaseAppException("object cannot be moved")