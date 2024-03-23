from abc import ABC, abstractmethod


class IVisitor(ABC):
    @abstractmethod
    def visit_circle(self, circle):
        """
        Visits a circle object.
        """
        raise NotImplementedError("Subclasses must implement the visit_circle method!")

    @abstractmethod
    def visit_square(self, square):
        """
        Visits a square object.
        """
        raise NotImplementedError("Subclasses must implement the visit_square method!")

    @abstractmethod
    def visit_rectangle(self, rectangle):
        """
        Visits a rectangle object.
        """
        raise NotImplementedError("Subclasses must implement the visit_rectangle method!")
