from abc import ABC, abstractmethod


class ITag(ABC):
    def __init__(self, content):
        self.content = content

    @abstractmethod
    def render(self):
        """
        Renders the content of a tag.
        """
        raise NotImplementedError("Subclasses must implement the render method!")