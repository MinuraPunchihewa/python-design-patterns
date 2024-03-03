from i_tag import ITag
from abc import ABC, abstractmethod


class IDecorator(ITag, ABC):
    def __init__(self, tag: ITag):
        self._tag = tag

    @abstractmethod
    def render(self):
        """
        Renders the content of a decorator.
        """
        raise NotImplementedError("Subclasses must implement the render method!")