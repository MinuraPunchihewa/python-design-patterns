from abc import ABC, abstractmethod

# may also be called Subscriber
class Observer(ABC):
    @abstractmethod
    def update(self, message: str) -> None:
        pass