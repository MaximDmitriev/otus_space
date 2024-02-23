from dataclasses import dataclass, field
from typing import Optional, List, Dict
import threading
from interfaces.scope import IScope

@dataclass
class Scope(IScope):
    name: str
    parent: Optional[IScope] = None
    children: List[IScope] = field(default_factory=list)
    strategy: Dict[str, callable] = field(default_factory=dict)

    def set_strategy(self, strategy):
        self.strategy = strategy

        return self
    
    def __iter__(self):
        self.__iter_out = self
        return self.__iter_out

    def __next__(self):
        """
        Метод для итерации для поиска команды по стратегиям
        """
        if self.__iter_out is None:
            raise StopIteration
        else:
            result = self.__iter_out
            self.__iter_out = self.__iter_out.parent
            return result
    


class ThreadData(threading.local):
    root_scope: Optional[IScope] = None
    current_scope: Optional[IScope] = None