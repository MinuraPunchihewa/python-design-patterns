from abc import ABC, abstractmethod


class IShape(ABC):
    @abstractmethod
    def accept(self, visitor):
        """
        Accepts a visitor object and calls the relevant visit method.
        """
        raise NotImplementedError("Subclasses must implement the accept method!")
