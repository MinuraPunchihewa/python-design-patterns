from factory import *


class ShapeFactory:
    @staticmethod
    def build_shape(shape: str) -> IShape:
        if shape.lower() == 'square':
            length = input("Enter the length of the Square: ")
            return Square(length)

        if shape.lower() == 'rectangle':
            length = input("Enter the length of the Rectangle: ")
            breadth = input("Enter the breadth of the Rectangle: ")
            return Rectangle(length, breadth)

# class ShapeFactory:
#     @staticmethod
#     def build_shape(shape: str, dimensions: dict) -> IShape:
#         return globals()[shape](dimensions)
