from interfaces.gameobject import GameObject
from commands.move import Move
from adapters.movable import MovableAdapter
from htypes.vector import Vector
from adapters.rotatable import RotatableAdapter
from commands.rotate import Rotate


def main():
    game_object = GameObject()
    
    game_object.set_property('location', Vector(12, 5))
    game_object.set_property('velocity', Vector(-7, 3))
    game_object.set_property('angular_velocity', -4)
    game_object.set_property('direction', 0)
    game_object.set_property('direction_numbers', 20)

    movable = MovableAdapter(game_object)
    move = Move(movable)

    rotatable = RotatableAdapter(game_object)
    rotate = Rotate(rotatable)

    try:
        move.execute()
        rotate.execute()
    except Exception as er:
        print(er)

    location = game_object.get_property('location')
    print(location.x, location.y)

    direction = game_object.get_property('direction')
    print(direction)


if __name__ == "__main__":
    main()