from builder import IShapeBuilder
from builder import Shape


class ShapeBuilder(IShapeBuilder):
    def __init__(self):
        self.shape = Shape()

    def set_type(self, type):
        self.shape.type = type
        return self

    def set_length(self, length):
        self.shape.length = length
        return self

    def set_breadth(self, breadth):
        self.shape.breadth = breadth
        return self

    def get_result(self):
        return self.shape
