from shape import Shape
from i_shape_builder import IShapeBuilder


class RectangleBuilder(IShapeBuilder):
    def __init__(self):
        self.shape = Shape()

    def set_type(self):
        self.shape.type = "Rectangle"

    def set_length(self):
        self.shape.length = 4

    def set_breadth(self):
        self.shape.breadth = 2