from factory.shape_factory import ShapeFactory
from builder import SquareDirector
from builder import RectangleDirector

if __name__ == "__main__":
    print("##### FACTORY #####")

    # build a square
    square = ShapeFactory.build_shape(
        'Square',
        {
            "length": 4
        }
    )

    print(square)
    print(square.perimeter())

    # build a rectangle
    rectangle = ShapeFactory.build_shape(
        'Rectangle',
        {
            "length": 6,
            "breadth": 5
        }
    )

    print(rectangle)
    print(rectangle.perimeter())

    print("### BUILDER ###")

    # construct a square
    square = SquareDirector.construct()

    print(square)

    # construct a rectangle
    rectangle = RectangleDirector.construct()

    print(rectangle)