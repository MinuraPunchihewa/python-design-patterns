from factory import *


class ShapeFactory:
    @staticmethod
    def build_shape(shape: str, dimensions: dict) -> IShape:
        return globals()[shape](dimensions)
