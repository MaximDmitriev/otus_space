import unittest
from adapters.movable import MovableAdapter
from adapters.rotatable import RotatableAdapter
from adapters.fuelable import FuelableAdapter
from commands.change_velocity import ChangeVelocity
from commands.move import Move
from commands.rotate import Rotate
from commands.macrocommand import MacroCommand
from commands.check_fuel import CheckFuel
from commands.burn_fuel import BurnFuel
from interfaces.gameobject import GameObject
from htypes.vector import Vector

class TestMacro(unittest.TestCase):
    '''тесты для макрокоманд'''

    def setUp(self):
        self.game_object = GameObject()
    
        movable = MovableAdapter(self.game_object)
        self.move = Move(movable)

        rotatable = RotatableAdapter(self.game_object)
        self.rotate = Rotate(rotatable)
        self.change_velocity = ChangeVelocity(rotatable)

        fuelable = FuelableAdapter(self.game_object)
        self.check_fuel = CheckFuel(fuelable)
        self.burn_fuel = BurnFuel(fuelable)

    def test_macro_error(self):
        '''при ошибке выбрасывает исключение'''

        macro = MacroCommand([self.move, self.rotate])

        with self.assertRaises(Exception):
            macro.execute()

    def test_move_burn_fuel(self):
        '''движение с сжиганием топлива'''
 
        self.game_object.set_property('location', Vector(12, 5))
        self.game_object.set_property('velocity', Vector(-7, 3))
        self.game_object.set_property('fuel_volume', 10)
        self.game_object.set_property('fuel_unit', 1)    

        macro = MacroCommand([self.check_fuel, self.burn_fuel, self.move])

        macro.execute()

        fuel_volume = self.game_object.get_property('fuel_volume')
        location = self.game_object.get_property('location')

        self.assertEqual(fuel_volume, 9)
        self.assertEqual(location, Vector(5, 8))


    def test_rotate_move(self):
        '''движение с поворотом'''
 
        self.game_object.set_property('location', Vector(12, 5))
        self.game_object.set_property('velocity', Vector(-7, 3))
        self.game_object.set_property('angular_velocity', -4)
        self.game_object.set_property('direction', 3)
        self.game_object.set_property('direction_numbers', 20)       

        macro = MacroCommand([self.rotate, self.change_velocity, self.move])

        macro.execute()

        velocity = self.game_object.get_property('velocity')
        location = self.game_object.get_property('location')

        self.assertEqual(location, Vector(-1, 7))
        self.assertEqual(velocity, Vector(-13, 2))
