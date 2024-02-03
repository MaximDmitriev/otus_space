from interfaces.command import Command
from interfaces.rotatable import Rotatable

class Rotate(Command):
    '''
    команда для поворота
    '''

    def __init__(self, obj: Rotatable) -> None:
        self.obj = obj

    def execute(self):
        try:
            direction = self.obj.get_direction()
        except:
            raise Exception("property 'direction' cannot be read")
        
        try:
            n = self.obj.get_direction_numbers()
        except:
            raise Exception("property 'direction_numbers' cannot be read")

        try:
            velocity = self.obj.get_angular_velocity()
        except:
            raise Exception("property 'angular_velocity' cannot be read")

        try:
            self.obj.set_direction((direction + velocity) % n)
        except:
            raise Exception("object cannot be rotated")