from abc import abstractmethod, ABC


class Movable(ABC):

    @abstractmethod
    def move(self):
        pass
