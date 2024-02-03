from math import isnan

class Vector:
    '''
    тип Vector
    '''
    
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __eq__(self, __value: object) -> bool:
        return self.x == __value.x and self.y == __value.y

    # def is_valid(self) -> bool:
    #     return isnan(self.x) or isnan(self.y)

    @classmethod
    def plus(cls, v1: 'Vector', v2: 'Vector') -> 'Vector':
        return cls(v1.x + v2.x, v1.y + v2.y)