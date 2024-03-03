from abc import ABC, abstractmethod


class IEmployee(ABC):
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary

    @abstractmethod
    def display(self, indent: int):
        pass