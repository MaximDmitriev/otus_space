from abc import ABC, abstractmethod

class IScope(ABC):
    @abstractmethod
    def set_strategy(self, strategy):
        pass