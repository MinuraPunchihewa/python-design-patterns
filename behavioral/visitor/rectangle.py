from visitor import IShape


class Rectangle(IShape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def accept(self, visitor):
        visitor.visit_rectangle(self)