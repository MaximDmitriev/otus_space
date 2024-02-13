from interfaces.gameobject import GameObject
from commands.move import Move
from adapters.movable import MovableAdapter
from htypes.vector import Vector
from adapters.rotatable import RotatableAdapter
from commands.rotate import Rotate
from queue import Queue
from errors.error_handler import ErrorHandler, BaseAppException
from commands.write_log import WriteLog
from commands.repeate import Repeate, RepeateHandler, DoubleRepeate

def main():
    game_object = GameObject()
    
    game_object.set_property('location', Vector(12, 5))
    # game_object.set_property('velocity', Vector(-7, 3))
    game_object.set_property('angular_velocity', -4)
    game_object.set_property('direction', 0)
    game_object.set_property('direction_numbers', 20)

    movable = MovableAdapter(game_object)
    move = Move(movable)

    rotatable = RotatableAdapter(game_object)
    rotate = Rotate(rotatable)



    queue = Queue()

    queue.put(move)
    queue.put(rotate)

    handler = ErrorHandler()

    # 2 раза повторить, затем запись в лог
    # handler.register(Move, BaseAppException, lambda cmd, exc: RepeatHandler(DoubleRepeate(cmd), queue))
    # handler.register(DoubleRepeate, BaseAppException, lambda cmd, exc: RepeatHandler(Repeate(cmd), queue))
    # handler.register(Repeate, BaseAppException, lambda cmd, exc: RepeatHandler(WriteLog(cmd, exc), queue))


    # повтор и запись в лог
    handler.register(Move, BaseAppException, lambda cmd, exc: RepeateHandler(Repeate(cmd), queue))
    handler.register(Repeate, BaseAppException, lambda cmd, exc: RepeateHandler(WriteLog(cmd, exc), queue))

    while not queue.empty():
        cmd = queue.get()
        try:
            cmd.execute()

        except Exception as err:
            exc = type(err)

            handler.handle(cmd, exc)

    # location = game_object.get_property('location')
    # print(location.x, location.y)

    # direction = game_object.get_property('direction')
    # print(direction)


if __name__ == "__main__":
    main()