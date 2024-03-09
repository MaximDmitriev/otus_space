from ioc.ioc import IoC
from interfaces.gameobject import GameObject
 

def get_methods(obj: object) -> iter:
    """ возвращает методы из интерфейса """

    props = [x for x in dir(obj) if not x.startswith('_')]

    props_obj = [obj.__getattribute__(obj, prop) for prop in props]
    return zip(props, props_obj)


def generate_init(self, name: str, obj: GameObject):
    """ генератор __init__ """

    self._obj = obj
    self._name = name


def generate_get(ioc: IoC, propname: str):
    """ генератор геттеров """

    def get_prop(self):
        return ioc.resolve(
            f'{self._name}.{self.__classname__.replace("Adapter", "")}.{str.capitalize(propname.split("_")[1])}.Get',
            self._obj
        )

    return get_prop


def generate_set(ioc: IoC, propname: str):
    """ генератор сеттеров """

    def set_prop(self, value):
        return ioc.resolve(
            f'{self._name}.{self.__classname__.replace("Adapter", "")}.{str.capitalize(propname.split("_")[1])}.Set',
            self._obj,
            value
        )

    return set_prop


class AdapterClass(type):
    """ Класс для генерации адаптеров по интерфейсам """

    def __new__(mcs, clsname, bases, attr):
        ioc = IoC()

        props = get_methods(attr['interface'])

        attrs = {
            '__init__': generate_init,
            '__classname__': clsname,
        }

        for propname, _ in props:
            attrs.update(
                {
                    propname: generate_set(ioc, propname) if 'set' in propname else generate_get(ioc, propname)
                }
            )

        return super(AdapterClass, mcs).__new__(mcs, clsname, bases, attrs)
