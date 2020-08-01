from abc import ABC, abstractmethod


class Figure(ABC):

    @abstractmethod
    def get_area(self) -> float:
        return 0.0

