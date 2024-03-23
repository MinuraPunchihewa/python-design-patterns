from i_shape import IShape


class Square(IShape):
    def __init__(self, length):
        self.length = length

    def accept(self, visitor):
        return visitor.visit_square(self)