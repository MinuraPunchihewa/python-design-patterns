from abc import ABC, abstractmethod


class IShapeBuilder(ABC):
    @staticmethod
    @abstractmethod
    def set_type():
        """
        Sets the type of a shape.
        """
        raise NotImplementedError("Subclasses must implement the set_type method!")

    @staticmethod
    @abstractmethod
    def set_length():
        """
        Sets the length of a shape.
        """
        raise NotImplementedError("Subclasses must implement the set_length method!")

    @staticmethod
    @abstractmethod
    def set_breadth():
        """
        Sets the breadth of a shape.
        """
        raise NotImplementedError("Subclasses must implement the set_breadth method!")
