from abc import ABC, abstractmethod


class IStrategy(ABC):
    @abstractmethod
    def sort(self, inputs):
        """
        Sorts the list of inputs.
        """
        raise NotImplementedError("Subclasses must implement the execute method!")
