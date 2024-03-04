from observer import Observer
from abc import ABC, abstractmethod

# may also be called Publisher
class Subject(ABC):
    def __init__(self) -> None:
        self._observers = []

    @abstractmethod
    def register(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def unregister(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self, message: str) -> None:
        pass