from visitor import IShape


class Circle(IShape):
    def __init__(self, radius):
        self.radius = radius

    def accept(self, visitor):
        visitor.visit_circle(self)