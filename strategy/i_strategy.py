from abc import ABC, abstractmethod


class IStrategy(ABC):
    @abstractmethod
    def execute(self, inputs):
        """
        Executes the strategy on the inputs.
        """
        raise NotImplementedError("Subclasses must implement the execute method!")
