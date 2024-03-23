from abc import ABC, abstractmethod


class ICollection(ABC):
    @abstractmethod
    def create_iterator(self):
        """
        Creates an iterator object.
        """
        raise NotImplementedError("Subclasses must implement the create_iterator method!")