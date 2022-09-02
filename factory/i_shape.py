from abc import ABC, abstractmethod


class IShape(ABC):
    @abstractmethod
    def perimeter(self):
        """
        Calculates the perimeter of a shape.
        """
        raise NotImplementedError("Subclasses must implement the perimeter method!")
