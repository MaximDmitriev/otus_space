from abc import ABC, abstractmethod

class Command(ABC):
    '''
    интерфейс для команд
    '''

    @abstractmethod
    def execute(self):
        ...