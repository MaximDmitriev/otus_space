import unittest
from adapters.generator import AdapterClass
from interfaces.movable import Movable
from commands.move import Move
from htypes.vector import Vector
from interfaces.gameobject import GameObject
from ioc.ioc import IoC

class TestAdapterGenerator(unittest.TestCase):
    ''' Тесты для генератора адаптеров '''

    def test_correct_object(self):
        ''' созданный адаптер корректно возвращает свойства объекта и выполняет команду'''
        
        ioc = IoC()
        object = GameObject()

        ioc.resolve(
            'ioc.register',
            'adapter.create',
            lambda interface, name, obj: AdapterClass(
                f'{interface.__name__}Adapter',
                (),
                {'interface': interface}
            )(name, obj)
        ).execute()


        adapter = ioc.resolve("adapter.create", Movable, 'SpaceShip', object)

        ioc.resolve('ioc.register', 'SpaceShip.Movable.Location.Get', lambda obj: obj.get_property('location')).execute()
        ioc.resolve('ioc.register', 'SpaceShip.Movable.Location.Set', lambda obj, value: obj.set_property('location', value)).execute()
        ioc.resolve('ioc.register', 'SpaceShip.Movable.Velocity.Get', lambda obj: obj.get_property('velocity')).execute()
        ioc.resolve('ioc.register', 'SpaceShip.Movable.Velocity.Set', lambda obj, value: obj.set_property('velocity', value)).execute()

        object.set_property('location', Vector(1, 1))
        object.set_property('velocity', Vector(6, 1))
        
        move = Move(adapter)
        move.execute()

        self.assertEqual(adapter.get_location(), Vector(7, 2))
        self.assertEqual(object.get_property('velocity'), adapter.get_velocity())
