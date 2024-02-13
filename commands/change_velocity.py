from math import cos, sin, pi
from typing import Union
from interfaces.command import Command
from interfaces.rotatable import Rotatable
from htypes.vector import Vector
from errors.error_handler import BaseAppException


class ChangeVelocity(Command):
    """
    Команда изменения вектора скорости при повороте
    """
    def __init__(self, obj: Rotatable):
        self.obj = obj

    def execute(self) -> None:
        if self.obj.get_velocity() != Vector(0, 0):
            try:
                d = self.obj.get_direction()
                n = self.obj.get_direction_numbers()
                v = self.obj.get_velocity()
            except Exception:
                raise BaseAppException("property cannot be read")

            try:
                self.obj.set_velocity(Vector(x=int(v.x + v.x * cos((2 * pi * d) / n)), y=int(v.y + v.y * sin((2 * pi * d) / n))))
            except Exception:
                raise BaseAppException("property cannot be set")
