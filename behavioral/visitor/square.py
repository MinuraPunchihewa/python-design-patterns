from visitor import IShape


class Square(IShape):
    def __init__(self, length):
        self.length = length

    def accept(self, visitor):
        visitor.visit_square(self)