from adapters.generator import AdapterClass
from interfaces.movable import Movable
from interfaces.gameobject import GameObject
from ioc.ioc import IoC
from htypes.vector import Vector
from commands.move import Move

ioc = IoC()

# возможно имеет смысл добавить в дефолтную стратегию
ioc.resolve(
    'ioc.register',
    'adapter.create',
    lambda interface, name, obj: AdapterClass(
        f'{interface.__name__}Adapter',
        (),
        {'interface': interface}
    )(name, obj)
).execute()

object = GameObject()

adapter = ioc.resolve("adapter.create", Movable, 'SpaceShip', object)

object.set_property('location', Vector(1, 1))
object.set_property('velocity', Vector(6, 1))

ioc.resolve('ioc.register', 'SpaceShip.Movable.Location.Get', lambda obj: obj.get_property('location')).execute()
ioc.resolve('ioc.register', 'SpaceShip.Movable.Location.Set', lambda obj, value: obj.set_property('location', value)).execute()
ioc.resolve('ioc.register', 'SpaceShip.Movable.Velocity.Get', lambda obj: obj.get_property('velocity')).execute()
ioc.resolve('ioc.register', 'SpaceShip.Movable.Velocity.Set', lambda obj, value: obj.set_property('velocity', value)).execute()

move = Move(adapter)
move.execute()

print(object.get_property('location').x, object.get_property('location').y)
print(object.get_property('velocity').x, object.get_property('velocity').y)

print(adapter.get_location().x)
print(object.get_property('location') == adapter.get_location())
