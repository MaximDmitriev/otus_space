from interfaces.movable import Movable
from interfaces.command import Command
from htypes.vector import Vector


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
            raise Exception("property 'location' cannot be read")

        
        try:
            velocity = self.obj.get_velocity()
        except:
            raise Exception("property 'velocity' cannot be read")


        try:
            self.obj.set_location(Vector.plus(location, velocity))
        except:
            raise Exception("object cannot be moved")